#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import math
from pathlib import Path

import chart_studio  # Stable as of 1.0.0
import plotly
import plotly.graph_objs as go  # Stable as of 4.1.1
from slugify import slugify

import shows
from show_continuity import Plot

OUTPUT_DIR = 'docs'


def get_continuity_edges(node_mouseover_texts, ep_to_posn, ep_to_idx, edge_data,
                         edge_line, curve_height_factor=1, flatten_adjacent=False,
                         from_text=None, to_text=None):
    '''Return a tuple including:
    * A list of edges (plotly Shapes) for a single kind of continuity, and
    * a Scatter trace of edge mouseover nodes (on midpoint of each edge)
    Also update the given list of episode node mouseover texts, based on the edges added to each node.
    Params:
        node_mouseover_texts: List of node mouseover texts to update
        node_posns: List of node posns
        ep_node_dict: Dict mapping episode numbers to their node positions
        edge_data: Iterable containing tuples of (from_ep, to_ep, description) or (from_ep, to_ep, level, description)
        edge_line: Dict optionally specifying standard edge properties (width, color, etc.)
        curve_height_factor: Factor controlling average height of the edge curves above the episode nodes. Negative to
                             draw edges below the episode nodes instead.
        flatten_adjacent: If True, connect adjacent episodes via a horizontal line instead of a Bezier curve.
        from_text: Optional format string for the mouseover text to be added to the 'from' episode node.
                   {from_ep} and {to_ep} will be replaced with respective episode numbers.
                   Default None.
        to_text: Optional format string for the mouseover text to be added to the 'to' episode node.
                 {from_ep} and {to_ep} will be replaced with respective episode numbers.
                 Default None.
    '''
    default_curve_height_factor = 0.5  # Arbitrarily chosen for aesthetics
    curve_height_factor *= default_curve_height_factor

    edges = []

    edge_mouseover_points_x = []
    edge_mouseover_points_y = []
    edge_mouseover_texts = []

    for from_ep, to_ep, level, *descriptions in edge_data:
        if from_ep not in ep_to_posn:
            print(f'Warning: Skipping data for unknown episode {repr(from_ep)}')
            continue
        elif to_ep not in ep_to_posn:
            print(f'Warning: Skipping data for unknown episode {repr(to_ep)}')
            continue

        x1, y1 = ep_to_posn[from_ep]
        x2, y2 = ep_to_posn[to_ep]
        euclidean_dist = math.hypot(x2 - x1, y2 - y1)

        if flatten_adjacent and ep_to_idx[to_ep] - ep_to_idx[from_ep] == 1:
            # Connect adjacent episodes by a horizontal line
            curve_control_point = ((x1 + x2) / 2, ((y1 + y2) / 2))
        else:
            # Calculate the Bezier curve's control point
            # As a rough experiment start with a scaling amount below the midpoint (should actually be
            # perpendicular away from the line connecting the two nodes but we're doing horizontal nodes for now)
            # TODO: Still need to decide how I want to visualize time travel. May end up putting them below the episodes
            #       whereas normal data will be above the episodes, in which case multiply height factor by -1 here
            #       If that's the case will need to separate out the foreshadowing graph though
            curve_control_point = ((x1 + x2) / 2,
                                   ((y1 + y2) / 2) + (curve_height_factor * euclidean_dist))

        # Add the edge
        edges.append(go.layout.Shape(
                type="path",
                path=f"M {x1},{y1} Q {curve_control_point[0]},{curve_control_point[1]} {x2},{y2}",
                line=edge_line))

        # Add a mouseover point/text to the edge. Default to the from_text if both provided
        if from_text is not None or to_text is not None:
            curve_midpoint_x = 0.25*x1 + 0.5*curve_control_point[0] + 0.25*x2
            curve_midpoint_y = 0.25*y1 + 0.5*curve_control_point[1] + 0.25*y2
            edge_mouseover_points_x.append(curve_midpoint_x)
            edge_mouseover_points_y.append(curve_midpoint_y)
            if from_text is not None:
                edge_mouseover_texts.append(f'{from_ep} ' + from_text.lower().format(to_ep=to_ep) + f'; {"; ".join(descriptions)}')
            elif to_text is not None:
                edge_mouseover_texts.append(f'{to_ep} ' + to_text.lower().format(from_ep=from_ep) + f'; {"; ".join(descriptions)}')

        # Add mouseover text to the 'to' nodes
        if to_text is not None:
            node_mouseover_texts[ep_to_idx[to_ep]] += \
                '<br>' + to_text.format(from_ep=from_ep) + f'; {"; ".join(descriptions)}'

    # Add mouseover text to the 'from' nodes (in a separate loop so incoming continuity is listed
    # before outgoing continuity within a given episode)
    if from_text is not None:
        for from_ep, to_ep, _, *descriptions in edge_data:
            if from_ep not in ep_to_idx or to_ep not in ep_to_idx:
                continue

            node_mouseover_texts[ep_to_idx[from_ep]] += \
                '<br>' + from_text.format(to_ep=to_ep) + f'; {"; ".join(descriptions)}'

    # Create a mouseover point in the middle of each edge, with the edge's description
    mouseovers_trace = go.Scatter(
            x=tuple(edge_mouseover_points_x),
            y=tuple(edge_mouseover_points_y),
            hoverinfo='text',
            hoverlabel=dict(align='left'),
            hovertext=tuple(edge_mouseover_texts),
            showlegend=False,
            mode='markers',
            marker=dict(
                color=edge_line['color'],
                opacity=0.5,
                size=1.5,
                line=dict(width=0)),  # The thickness of the node's border line
            visible=True)

    return edges, mouseovers_trace


def plot_show_continuity(show, args):
    '''Generate an html file graphing continuity in the given show, opening it when done.'''

    # Create a dict mapping episode IDs to XY positions on the horizontal axis
    ep_to_posn = {ep_id: (i, 0) for i, ep_id in enumerate(show.episodes().keys())}
    # Create a dict mapping episode IDs to their ordered index
    ep_to_idx = {ep_id: i for i, ep_id in enumerate(show.episodes().keys())}

    # Create the episode nodes graph object
    node_trace = go.Scatter(x=tuple(p[0] for p in ep_to_posn.values()),
                            y=tuple(p[1] for p in ep_to_posn.values()),
                            hoverinfo='none',
                            showlegend=False,
                            mode='markers',
                            marker=dict(
                                color=[],
                                size=5,
                                line=dict(width=0.5)),  # The thickness of the node's border line
                            visible=True)

    # Color nodes by season
    node_colors = []
    for season_info in show.seasons.values():
        node_colors.extend(len(season_info['episodes']) * [season_info['color']])
    node_trace['marker']['color'] = tuple(node_colors)

    # Create mouseover text for each node. We'll update the mouseover text for each episode based
    # on its edge connections
    mouseover_texts = [f'<b>{ep_id}: {ep_title}</b>'
                       for ep_id, ep_title in show.episodes().items()]

    # Add edges
    edge_traces = []
    mouseover_traces = []
    legend_traces = []

    # Filter out referential vs causal vs serial plot threads
    referential_threads, causal_threads, serial_threads = [], [], []
    for plot_thread in show.plot_threads:
        if plot_thread[2] == Plot.REFERENTIAL:
            referential_threads.append(plot_thread)
        elif plot_thread[2] == Plot.CAUSAL:
            causal_threads.append(plot_thread)
        elif plot_thread[2] == Plot.SERIAL:
            serial_threads.append(plot_thread)

    # Note: Order here determines order of appearance in mouseover text
    for plot_threads, edge_line, to_text in ((serial_threads, dict(color='black', width=1), 'Continues {from_ep}'),
                                             (causal_threads, dict(color='black', width=0.5), 'Caused by {from_ep}'),
                                             (referential_threads, dict(color='black', width=0.25), 'References {from_ep}')):
        if plot_threads:
            line = dict(color='black', width=0.5)
            plot_edges, plot_mouseovers = get_continuity_edges(
                    node_mouseover_texts=mouseover_texts,
                    ep_to_posn=ep_to_posn, ep_to_idx=ep_to_idx,
                    edge_data=plot_threads,
                    edge_line=edge_line,
                    flatten_adjacent=True,
                    to_text=to_text)
            edge_traces.extend(plot_edges)
            mouseover_traces.append(plot_mouseovers)

    # Add a dummy line trace to create a corresponding legend item (plotly Shapes don't legendify)
    # I could legendify each of serial, causal, and referential, but the appearances get kind of messed up whenever
    # there are multiple plot threads between 2 episodes, so it could end up more misleading than letting users infer
    # the 'importance'.
    legend_traces.append(go.Scatter(x=(None,), y=(None,), mode='lines', hoverinfo='none',
                                   name='Plot Threads',
                                   line=dict(color='black', width=0.5),
                                   visible=True))

    if show.foreshadowing:
        foreshadowing_line = dict(color='blue', width=0.375)
        foreshadowing_edges, foreshadowing_mouseovers = get_continuity_edges(
                node_mouseover_texts=mouseover_texts,
                ep_to_posn=ep_to_posn, ep_to_idx=ep_to_idx,
                edge_data=show.foreshadowing,
                edge_line=foreshadowing_line,
                curve_height_factor=-1,  # below the episode nodes
                flatten_adjacent=False,
                from_text='Foreshadows {to_ep}',
                to_text='Foreshadowed by {from_ep}')
        edge_traces.extend(foreshadowing_edges)
        mouseover_traces.append(foreshadowing_mouseovers)
        # Add a dummy line trace to create a corresponding legend item (plotly Shapes don't legendify)
        legend_traces.append(go.Scatter(x=(None,), y=(None,), mode='lines', hoverinfo='none',
                                       name='Foreshadowing',
                                       line=foreshadowing_line,
                                       visible=True))

    # Prepare the figure layout for the plots
    fig_layout = go.Layout(
        title=dict(text=f'<br><b>Continuity in {show.title}</b>',
                   font=dict(color='black', size=16), x=0.5),
        showlegend=True,
        legend=dict(x=0.9, y=0.95, itemclick=False, itemdoubleclick=False),
        # If hovermode is set to 'closest', it picks any node close enough to the mouse's position
        # If set to e.g. 'x', picks the node (any distance away) which is closest to the mouse's x
        # position.
        hovermode='closest',
        dragmode='pan', # Default mouse mode
        margin=dict(b=5, l=5, r=5, t=40, pad=0),
        plot_bgcolor='white',
        # Maintain the x-y ratio so the curves look 'nice' regardless of screen size
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False,
                   scaleanchor='x', scaleratio=1),
        shapes=edge_traces)

    base_file_name = slugify(show.brief_title)

    if not args.spoilers:
        plot_name = f'{base_file_name}_no_spoilers_continuity_graph'
        fig_traces = [node_trace] + legend_traces
    else:
        plot_name = f'{base_file_name}_continuity_graph'

        # Add the node mouseover data
        # Add node mouseover text to the node trace
        node_trace.hoverinfo = 'text'
        node_trace.hoverlabel = dict(align='left')
        node_trace.hovertext = tuple(mouseover_texts)
        # Add some helper text mentioning the existence of mouseover info
        fig_layout.annotations = [
            dict(text="Hover over nodes/edges to see details.",
                 showarrow=False,
                 xref="paper", yref="paper",
                 x=1.0, y=1.0)]

        fig_traces = [node_trace] + mouseover_traces + legend_traces

    fig = go.Figure(data=fig_traces, layout=fig_layout)

    if args.publish:
        chart_studio.plotly.plot(fig, filename=plot_name, sharing='public')
    else:
        plotly.offline.plot(fig, filename=str(Path(OUTPUT_DIR) / (plot_name + '.html')), show_link=False,
                            auto_open=True)


def plot_show_serialities(shows, args):
    '''Plot an [Episodic <--> Serial] line chart with labelled nodes for all given shows.'''
    # Plot a vertical line from 0 to 1
    line_trace = go.Scatter(x=(0, 0), y=(0, 1), mode='lines',  # (0,0) to (1, 0)
                            line=dict(width=0.5, color='black'),
                            hoverinfo='none')

    # Add labelled markers to the ends of the line
    line_ends_trace = go.Scatter(x=(0, 0), y=(0, 1),
                                 text=('Episodic', 'Serial'),
                                 hoverinfo='none',
                                 mode='markers+text',
                                 textposition=("bottom center", "top center"),
                                 textfont=dict(size=18),
                                 marker=dict(
                                     symbol='line-ew',
                                     color=[],
                                     size=5,
                                     line=dict(width=1)))

    # Sort shows by seriality and bucket any that are too close together
    shows_data = [(s.seriality_score(), s.brief_title) for s in shows]
    shows_data.sort()

    bucketed_data = []
    last_score = -1
    for score, title in shows_data:
        if score - last_score < 0.02:
            bucketed_data[-1].append((score, title))
        else:
            bucketed_data.append([(score, title)])
            last_score = score  # only updated for first score of bucket so buckets don't increase past 0.02 size

    # Add a node for each bucket (with title(s) on the right)
    nodes_x = tuple(0 for _ in bucketed_data)
    nodes_y = tuple(bucket[0][0] for bucket in bucketed_data)
    nodes_trace = go.Scatter(x=nodes_x, y=nodes_y,
                             text=tuple(', '.join(x[1] for x in bucket) for bucket in bucketed_data),
                             hoverinfo='none',
                             mode='markers+text',
                             textposition='middle right',
                             marker=dict(
                                 color='black',
                                 size=5,
                                 line=dict(width=1)))  # The thickness of the node's border line

    # Add labels of the seriality percentages on the left. Label buckets with min and max scores in them if necessary
    score_labels = []
    for bucket in bucketed_data:
        min_percent = f'{100 * bucket[0][0]:.0f}'  # Rounds to nearest %
        max_percent = f'{100 * bucket[-1][0]:.0f}'
        if min_percent == max_percent:  # 1-size bucket or multiple shows with same rounded score
            score_labels.append(f'{min_percent}% ')
        else:
            score_labels.append(f'{min_percent}-{max_percent}% ')
    percentage_labels_trace = go.Scatter(
        x=nodes_x, y=nodes_y,
        text=tuple(score_labels),
        hoverinfo='none',
        mode='text',
        textposition='middle left')

    # Prepare the figure layout for the plot
    title = args.title if args.title else 'Show Serialities'
    fig_layout = go.Layout(
        title=dict(text=f"<br><b>{title}</b>",
                   font=dict(color='black', size=16),
                   x=0.5),
        showlegend=False,
        dragmode='pan',  # Default mouse mode
        margin=dict(b=5, l=5, r=5, t=40, pad=0),
        plot_bgcolor='white',
        xaxis=dict(showgrid=True, zeroline=True, showticklabels=False),
        yaxis=dict(showgrid=True, zeroline=True, showticklabels=False))

    fig = go.Figure(data=[line_trace, line_ends_trace, nodes_trace, percentage_labels_trace], layout=fig_layout)

    plot_filename = slugify(title)

    if args.publish:
        chart_studio.plotly.plot(fig, filename=plot_filename, sharing='public')
    else:
        plotly.offline.plot(fig, filename=str(Path(OUTPUT_DIR) / (plot_filename + '.html')), show_link=False,
                            auto_open=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(dest='show_data_modules', nargs='*', type=str,
                        default=shows.__all__,
                        help="The python module(s) to import show data from.")
    parser.add_argument('--spoilers', action='store_true',
                        help="Include mouseover text with episode titles / connection descriptions")
    parser.add_argument('--title', type=str,
                        help="Title of the chart to create. Only used for the --serialities chart"
                             + " as individual show graphs have deterministic titles based on the show's title.")
    parser.add_argument('--publish', action='store_true', dest="publish", default=False,
                        help="Publicly publish the plot to the preset plotly profile.")
    parser.add_argument('--serialities', action='store_true', default=False,
                        help="Plot the given shows' seriality scores on a line.")
    args = parser.parse_args()

    if args.title and not args.serialities:
        parser.error("--title may only be used with --serialities")

    # Create the output directory if it does not exist
    (Path(__file__).parent / OUTPUT_DIR).mkdir(exist_ok=True)

    shows = [__import__(f'shows.{show_module_name}', fromlist=['show']).show
             for show_module_name in args.show_data_modules]

    if args.serialities:
        print(f'Creating seriality plot...')
        plot_show_serialities(shows=(show for show in shows), args=args)
    else:
        for show in shows:
            print(f'Creating continuity plot for {show.title}...')
            plot_show_continuity(show=show, args=args)

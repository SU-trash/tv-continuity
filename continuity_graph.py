#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import copy
import math
from pathlib import Path

import chart_studio  # Stable as of 1.0.0
import plotly
import plotly.graph_objs as go  # Stable as of 4.1.1
from slugify import slugify

import shows

OUTPUT_DIR = 'output'


def get_continuity_edges(node_mouseover_texts, ep_to_posn, ep_to_idx, edge_data,
                         line, curve_height_factor=1, flatten_adjacent=False,
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
        line: Dict optionally specifying standard edge properties (width, color, etc.)
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

    for from_ep, to_ep, level, description in edge_data:
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
        edge_line = copy.copy(line)
        if level is not None:
            edge_line['width'] *= level / 2  # Scale width based on continuity 'level' with 2 being default size
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
                edge_mouseover_texts.append(f'Ep {from_ep} ' + from_text.lower().format(to_ep=to_ep) + f'; {description}')
            elif to_text is not None:
                edge_mouseover_texts.append(f'Ep {to_ep} ' + to_text.lower().format(from_ep=from_ep) + f'; {description}')

        # Add mouseover text to the 'to' nodes
        if to_text is not None:
            node_mouseover_texts[ep_to_idx[to_ep]] += \
                '<br>' + to_text.format(from_ep=from_ep) + f'; {description}'

    # Add mouseover text to the 'from' nodes (in a separate loop so incoming continuity is listed
    # before outgoing continuity within a given episode)
    if from_text is not None:
        for from_ep, to_ep, _, description in edge_data:
            if from_ep not in ep_to_idx or to_ep not in ep_to_idx:
                continue

            node_mouseover_texts[ep_to_idx[from_ep]] += \
                '<br>' + from_text.format(to_ep=to_ep) + f'; {description}'

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
                color=line['color'],
                opacity=0.5,
                size=1.5,
                line=dict(width=0)),  # The thickness of the node's border line
            visible=True)

    return edges, mouseovers_trace


def plot_show_continuity(show, args):
    '''Generate an html file graphing continuity in the given show, opening it when done.'''

    # Create a dict mapping episode IDs to XY positions on the horizontal axis
    ep_to_posn = {ep_id: (i, 0) for i, ep_id in enumerate(show.episodes.keys())}
    # Create a dict mapping episode IDs to their ordered index
    ep_to_idx = {ep_id: i for i, ep_id in enumerate(show.episodes)}

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
        node_colors.extend(min(season_info['num_eps'],
                               len(ep_to_posn) - len(node_colors))
                           * [season_info['color']])
    node_trace['marker']['color'] = tuple(node_colors)

    # Create mouseover text for each node. We'll update the mouseover text for each episode based
    # on its edge connections
    mouseover_texts = [f'<b>Ep {ep_id}: {ep_title}</b>'
                       for ep_id, ep_title in show.episodes.items()]

    # Add edges
    edge_traces = []
    mouseover_traces = []
    legend_traces = []

    if show.plot_threads:
        plot_line = dict(color='black', width=0.5)
        plot_edges, plot_mouseovers = get_continuity_edges(
                node_mouseover_texts=mouseover_texts,
                ep_to_posn=ep_to_posn, ep_to_idx=ep_to_idx,
                edge_data=show.plot_threads,
                line=plot_line,
                curve_height_factor=1,  # above the episode nodes
                flatten_adjacent=True,
                to_text='Continues plot of ep {from_ep}')
        edge_traces.extend(plot_edges)
        mouseover_traces.append(plot_mouseovers)
        # Add a dummy line trace to create a corresponding legend item (plotly Shapes don't legendify)
        legend_traces.append(go.Scatter(x=(None,), y=(None,), mode='lines', hoverinfo='none',
                                       name='Plot Threads',
                                       line=plot_line,
                                       visible=True))

    if show.foreshadowing:
        foreshadowing_line = dict(color='blue', width=0.375)
        foreshadowing_edges, foreshadowing_mouseovers = get_continuity_edges(
                node_mouseover_texts=mouseover_texts,
                ep_to_posn=ep_to_posn, ep_to_idx=ep_to_idx,
                edge_data=show.foreshadowing,
                line=foreshadowing_line,
                curve_height_factor=-1,  # below the episode nodes
                flatten_adjacent=False,
                from_text='Foreshadows ep {to_ep}',
                to_text='Foreshadowed by ep {from_ep}')
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

    if args.no_spoilers:
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
                 x=1.0, y=1.0)
        ]

        fig_traces = [node_trace] + mouseover_traces + legend_traces

    fig = go.Figure(data=fig_traces, layout=fig_layout)

    if args.publish:
        chart_studio.plotly.plot(fig, filename=plot_name, sharing='public')
    else:
        plotly.offline.plot(fig, filename=str(Path(OUTPUT_DIR) / (plot_name + '.html')), show_link=False,
                            auto_open=True)


def plot_show_serialities(shows):
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

    # Add a node for each show (with title on the right)
    shows_data = [(s.seriality_score(), s.brief_title) for s in shows]
    scores, titles = zip(*shows_data) if shows_data else ((), ())  # Inverse zip assignment breaks if data is empty
    nodes_trace = go.Scatter(x=tuple(0 for _ in scores),
                             y=scores,
                             text=titles,
                             hoverinfo='none',
                             mode='markers+text',
                             textposition='middle right',
                             marker=dict(
                                 color='black',
                                 size=5,
                                 line=dict(width=1)))  # The thickness of the node's border line

    # Add labels of the seriality percentages on the left
    percentage_labels_trace = go.Scatter(
        x=tuple(0 for _ in scores),
        y=scores,
        text=tuple(f'{100 * score:.1f}% ' for score in scores),
        hoverinfo='none',
        mode='text',
        textposition='middle left')

    # Prepare the figure layout for the plot
    fig_layout = go.Layout(
        title=dict(text=f"<br><b>Show Serialities</b>",
                   font=dict(color='black', size=16), x=0.5),
        showlegend=False,
        dragmode='pan',  # Default mouse mode
        margin=dict(b=5, l=5, r=5, t=40, pad=0),
        plot_bgcolor='white',
        xaxis=dict(showgrid=True, zeroline=True, showticklabels=False),
        yaxis=dict(showgrid=True, zeroline=True, showticklabels=False))

    fig = go.Figure(data=[line_trace, line_ends_trace, nodes_trace, percentage_labels_trace], layout=fig_layout)

    plot_name = 'show_serialities_chart'
    plotly.offline.plot(fig, filename=str(Path(OUTPUT_DIR) / (plot_name + '.html')), show_link=False, auto_open=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(dest='show_data_modules', nargs='*', type=str,
                        default=shows.__all__,
                        help="The python module(s) to import show data from.")
    parser.add_argument('--no-spoilers', action='store_true', default=False,
                        dest="no_spoilers",
                        help="Additionally create a plot with no mouseover text"
                             + " (episode titles / connection descriptions)")
    parser.add_argument('--publish', action='store_true', dest="publish", default=False,
                        help="Publicly publish the plot to the preset plotly profile.")
    parser.add_argument('--serialities', action='store_true', default=False,
                        help="Plot the given shows' seriality scores on a line.")
    args = parser.parse_args()

    # Create the output directory if it does not exist
    (Path(__file__).parent / OUTPUT_DIR).mkdir(exist_ok=True)

    shows = [__import__(f'shows.{show_module_name}', fromlist=[f'show']).show
             for show_module_name in args.show_data_modules]

    if args.serialities:
        print(f'Creating seriality plot...')
        plot_show_serialities(show for show in shows if show.episodes)
    else:
        for show in shows:
            print(f'Creating continuity plot for {show.title}...')
            plot_show_continuity(show, args)

#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# TODO: Priority List:
# - Hide or fade to background edges that don't touch the node currently being hovered over
#   Dash app allows this but is fairly heavy, code and performance-wise
# - Clean up spaghetti code when plotly finally allows Shapes in the legend:
#   https://github.com/plotly/plotly.js/issues/98
# - link of some sort on clicking on an episode node - e.g. that episode's wikia page?

import argparse
import copy
import math
from pathlib import Path

import chart_studio  # Stable as of 1.0.0
import plotly
import plotly.graph_objs as go  # Stable as of 4.1.1

import shows

OUTPUT_DIR = 'output'


def linear_positions(N):
    '''Return an iterable of n positions (tuples) forming a line on the x-axis. First and
    last positions are always (-1, 0) and (1, 0).
    '''
    # Edge case to avoid dividing by 0
    if N == 1:
        yield -1.0, 0.0
    else:
        for i in range(N):
            # Lay them out left-to-right from -1 to 1
            yield -1 + i * 2 / (N - 1), 0


def get_episode_node_dict(episodes):
    '''Given a dict of number:title of episodes, where number is either an integer or a string of
    multiple integers formatted as 'i/i+1' or 'i-j' (for multi-part episodes), return a convenience
    dict that maps any episode number/string to its relative position in the list of nodes.
    E.g. for episodes [1, 2/3, 4], episode 4 is only the third node.
    This gives a bit of flexibility in how the edges reference multi-part episodes.
    '''
    episode_node_dict = {}
    for i, ep_num in enumerate(episodes.keys()):
        episode_node_dict[ep_num] = i
        if isinstance(ep_num, str):
            start_ep, end_ep = ep_num.replace('/', '-').split('-')
            for j in range(int(start_ep), int(end_ep) + 1):
                episode_node_dict[j] = i
    return episode_node_dict


def get_continuity_edges(node_mouseover_texts, node_posns, ep_node_dict, data,
                         line, curve_height_factor=1,
                         from_text=None, to_text=None):
    '''Return a tuple including:
    * A list of edges (plotly Shapes) for a single kind of continuity, and
    * a Scatter trace of edge mouseover nodes (on midpoint of each edge)
    Also update the given list of episode node mouseover texts, based on the edges added to each node.
    Params:
        node_mouseover_texts: List of node mouseover texts to update
        node_posns: List of node posns
        ep_node_dict: Dict mapping episode numbers to their node positions
        data: Iterable of edge data, containing tuples of (from_ep, to_ep, descr) or (from_ep, to_ep, level, descr)
        line: Dict optionally specifying standard edge properties (width, color, etc.)
        curve_height_factor: Factor controlling average height of the edge curves above the episode nodes. Negative to
                             draw edges below the episode nodes instead.
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

    for datum in data:
        if len(datum) == 3:
            from_ep, to_ep, description = datum
            level = None
        else:
            from_ep, to_ep, level, description = datum
        if from_ep not in ep_node_dict:
            print(f'Warning: Skipping data for unknown episode {repr(from_ep)}')
            continue
        elif to_ep not in ep_node_dict:
            print(f'Warning: Skipping data for unknown episode {repr(to_ep)}')
            continue

        x1, y1 = node_posns[ep_node_dict[from_ep]]
        x2, y2 = node_posns[ep_node_dict[to_ep]]
        euclidean_dist = math.hypot(x2 - x1, y2 - y1)
        # Calculate the Bezier curve's control point
        # As a rough experiment start with a scaling amount below the midpoint (should actually be
        # perpendicular away from a connecting the two nodes but whatever for now)
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
            node_mouseover_texts[ep_node_dict[to_ep]] += \
                '<br>' + to_text.format(from_ep=from_ep) + f'; {description}'

    # Add mouseover text to the 'from' nodes (in a separate loop so incoming continuity is listed
    # before outgoing continuity within a given episode)
    if from_text is not None:
        for datum in data:
            if len(datum) == 3:
                from_ep, to_ep, description = datum
            else:
                from_ep, to_ep, _, description = datum

            if from_ep not in ep_node_dict or to_ep not in ep_node_dict:
                continue

            node_mouseover_texts[ep_node_dict[from_ep]] += \
                '<br>' + from_text.format(to_ep=to_ep) + f'; {description}'

    # Create the edge mouseover nodes from the collected data
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


def plot_show_continuity(show, args, base_file_name):
    '''Generate an html file graphing continuity in the given show, and open it when done.
    '''
    print(f'Creating continuity plot for {show.title}...')

    # Add nodes for episodes to the graph
    print('    Adding episode nodes...', flush=True)

    node_trace = go.Scatter(x=(), y=(),
        hoverinfo='none',
        showlegend=False,
        mode='markers',
        marker=dict(
            color=[],
            size=5,
            line=dict(width=1)),  # The thickness of the node's border line
        visible=True)

    # Get the node posns arranged in a horizontal line
    node_posns = tuple(linear_positions(len(show.episodes)))
    node_trace['x'], node_trace['y'] = zip(*node_posns)

    # Pre-process the episodes data for later convenience
    ep_node_dict = get_episode_node_dict(show.episodes)

    # Color nodes by season
    node_colors = []
    for season_info in show.seasons.values():
        start = ep_node_dict[season_info['start']]
        if 'end' in season_info:
            end = ep_node_dict[season_info['end']]
        else: # If the season hasn't yet ended:
            end = len(show.episodes)
        num_ep_nodes = end - start + 1
        node_colors.extend(num_ep_nodes * [season_info['color']])
    node_trace['marker']['color'] = tuple(node_colors)

    # Create mouseover text for each node. We'll update the mouseover text for each episode based
    # on its edge connections
    mouseover_texts = [f'<b>Ep {ep_num}: {ep_title}</b>'
                       for ep_num, ep_title in show.episodes.items()]

    print('    Adding edges...', flush=True)
    edge_traces = []
    mouseover_traces = []
    legend_traces = []

    # Plot threads
    plot_line = dict(color='black', width=0.5)
    plot_edges, plot_mouseovers = get_continuity_edges(
            mouseover_texts, node_posns, ep_node_dict,
            data=show.plot_threads,
            line=plot_line,
            curve_height_factor=1,  # above the episode nodes
            to_text='Continues plot of ep {from_ep}')
    edge_traces.extend(plot_edges)
    mouseover_traces.append(plot_mouseovers)
    # Add a dummy line trace to create a corresponding legend item (plotly Shapes don't legendify)
    legend_traces.append(go.Scatter(x=(None,), y=(None,), mode='lines', hoverinfo='none',
                                   name='Plot Threads',
                                   line=plot_line,
                                   visible=True))

    # Foreshadowing
    foreshadowing_line = dict(color='blue', width=0.375)
    foreshadowing_edges, foreshadowing_mouseovers = get_continuity_edges(
            mouseover_texts, node_posns, ep_node_dict,
            data=show.foreshadowing,
            line=foreshadowing_line,
            curve_height_factor=-1,  # below the episode nodes
            from_text='Foreshadows ep {to_ep}',
            to_text='Foreshadowed by ep {from_ep}')
    edge_traces.extend(foreshadowing_edges)
    mouseover_traces.append(foreshadowing_mouseovers)
    # Add a dummy line trace to create a corresponding legend item (plotly Shapes don't legendify)
    legend_traces.append(go.Scatter(x=(None,), y=(None,), mode='lines', hoverinfo='none',
                                   name='Foreshadowing',
                                   line=foreshadowing_line,
                                   visible=True))

    print('    Plotting the figure with Plotly...', flush=True)
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
        # Maintain the x-y ratio so the plot is a semicircle regardless of screen size
        # Setting range from xaxis doesn't seem to allow below [-2, 2], but setting yaxis works...
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False,
                   scaleanchor='x', scaleratio=1, range=[-0.5, 0.5]),
        shapes=edge_traces)

    if args.add_spoiler_free_plot:
        print('    Plotting the spoiler-free figure with Plotly...', flush=True)

        spoiler_free_fig = go.Figure(data=[node_trace] + legend_traces,
                                     layout=fig_layout)

        no_spoilers_plot_name = base_file_name + '_no_spoilers_continuity_graph'
        if not args.publish:
            plotly.offline.plot(spoiler_free_fig, filename=str(Path(OUTPUT_DIR) / (no_spoilers_plot_name + '.html')),
                                show_link=False, auto_open=True)
        else:
            chart_studio.plotly.plot(spoiler_free_fig, filename=no_spoilers_plot_name, sharing='public')

    # Add the node mouseover data now that we're done with the spoiler-free plot
    # Add node mouseover text to the node trace, now that we're done updating them with edge data
    node_trace.hoverinfo = 'text'
    node_trace.hoverlabel = dict(align='left')
    node_trace.hovertext = tuple(mouseover_texts)
    # Add some helper text to the spoiler version mentioning the existence of mouseover info
    fig_layout.annotations = [
        dict(text="Hover over nodes/edges to see details.",
             showarrow=False,
             xref="paper", yref="paper",
             x=1.0, y=1.0)
    ]

    fig = go.Figure(data=[node_trace] + mouseover_traces + legend_traces,
                    layout=fig_layout)

    plot_name = base_file_name + '_continuity_graph'
    if not args.publish:
        plotly.offline.plot(fig, filename=str(Path(OUTPUT_DIR) / (plot_name + '.html')), show_link=False, auto_open=True)
    else:
        chart_studio.plotly.plot(fig, filename=plot_name, sharing='public')

    print('    Done.')


def plot_show_serialities(shows):
    if not shows:
        raise Exception("No shows specified")

    '''Plot an [Episodic <--> Serial] line chart with labelled nodes for all given shows.'''
    # Plot a line from 0 to 1
    line_trace = go.Scatter(x=(0, 1), y=(0, 0), mode='lines',  # (0,0) to (1, 0)
                            line=dict(width=0.5, color='black'),
                            hoverinfo='none',
                            visible=True)

    # Add labelled markers to the ends of the line
    line_ends_trace = go.Scatter(x=(0, 1), y=(0, 0),
                                 text=('Episodic', 'Serial'),
                                 hoverinfo='none',
                                 mode='markers+text',
                                 textposition=("middle left", "middle right"),
                                 textfont=dict(size=18),
                                 marker=dict(
                                     symbol='line-ns',
                                     color=[],
                                     size=5,
                                     line=dict(width=1)),
                                 visible=True)

    # Add nodes for each show
    # TODO: Should really move to matplotlib since it probably isn't missing basic frickin features like
    #       angled text on markers. Annotations can be angled but they don't respect pan/zoom.
    data = [(s.seriality_score(), f'{s.brief_title}: {100 * s.seriality_score():.1f}%') for s in shows]
    # Sort the shows by seriality so we can alternate their text positions above vs below the line
    # Avoids most text overlap conflicts
    data.sort(key=lambda s: s[0])
    seriality_scores, titles = zip(*data) # Note: inverse zip assignment breaks if data is empty
    nodes_trace = go.Scatter(x=tuple(seriality_scores),
                             y=tuple(0 for _ in shows),
                             text=tuple(titles),
                             hoverinfo='none',
                             mode='markers+text',
                             textposition=((len(shows) // 2) * ("top center", "bottom center")
                                           + (len(shows) % 2) * ("top center",)),
                             marker=dict(
                                 color=[],
                                 size=5,
                                 line=dict(width=1)),  # The thickness of the node's border line
                             visible=True)

    # Prepare the figure layout for the plot
    fig_layout = go.Layout(
        title=dict(text=f"<br><b>Show Serialities</b>",
                   font=dict(color='black', size=16), x=0.5),
        showlegend=False,
        # If hovermode is set to 'closest', it picks any node close enough to the mouse's position
        # If set to e.g. 'x', picks the node (any distance away) which is closest to the mouse's x
        # position.
        hovermode='closest',
        dragmode='pan',  # Default mouse mode
        margin=dict(b=5, l=5, r=5, t=40, pad=0),
        plot_bgcolor='white',
        xaxis=dict(showgrid=True, zeroline=True, showticklabels=False),
        yaxis=dict(showgrid=True, zeroline=True, showticklabels=False),
        shapes=[])

    fig = go.Figure(data=[line_trace, line_ends_trace, nodes_trace], layout=fig_layout)

    plot_name = 'show_serialities_chart'
    plotly.offline.plot(fig, filename=str(Path(OUTPUT_DIR) / (plot_name + '.html')), show_link=False, auto_open=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(dest='show_data_modules', nargs='*', type=str,
                        default=shows.__all__,
                        help="The python module(s) to import show data from.")
    parser.add_argument('--add-spoiler-free-plot', action='store_true', default=False,
                        dest="add_spoiler_free_plot",
                        help="Additionally create a plot with no mouseover text"
                             + " (episode titles / connection descriptions)")
    parser.add_argument('--publish', action='store_true', dest="publish", default=False,
                        help="Publicly publish the plot to the preset plotly profile.")
    args = parser.parse_args()

    # Create the output directory if it does not exist
    (Path(__file__).parent / OUTPUT_DIR).mkdir(exist_ok=True)

    for show_module_name in args.show_data_modules:
        # Import show data from the given module
        show = __import__(f'shows.{show_module_name}', fromlist=[f'show']).show

        plot_show_continuity(show, args, base_file_name=show_module_name)

    plot_show_serialities([__import__(f'shows.{show_module_name}', fromlist=[f'show']).show
                           for show_module_name in args.show_data_modules])

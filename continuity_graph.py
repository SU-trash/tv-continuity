#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# TODO: Priority List:
# - Allow loading the show data in dynamically and agnostically
# - Modify mouseover text when foreshadowing/callbacks/plot threads traces are disabled
# - Add a way to view a single season at a time (with nodes redistributed into a new semicircle)
#   Alternatively, just make some separate per-season graphs
# - Prevent episode nodes from being hidden by plotly on legend double-click (hides all but one
#   trace, but also hides traces that were hidden from the legend)
# - See if any use for plotly's 'legendgroup' can be found in future extensions of this
# - Hide or fade to background edges that don't touch the node currently being hovered over

print('Loading libraries...', flush=True)

import argparse
import math
import numpy as np

import chart_studio # Stable as of 1.0.0
import plotly
import plotly.graph_objs as go # Stable as of 4.1.1

def semicircular_positions(N):
    '''Return an iterable of n positions (tuples) forming a semicircle on the unit circle. First and
    last positions are always (-1, 0) and (1, 0).
    '''
    # Edge case to avoid dividing by 0
    if N == 1:
        yield (-1.0, 0.0)
    else:
        for i in range(N):
            # Calculate the angle of this position in radians
            theta = math.pi * (N - 1 - i) / (N - 1)
            yield (math.cos(theta), math.sin(theta))


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


def get_continuity_edge_trace(mouseover_texts, node_posns, ep_node_dict, data,
                              legend_name, edge_color, visible=True,
                              to_text=None, from_text=None):
    '''Create a trace of edges for a single kind of continuity. Update the given list of mouseover
    texts accordingly.
    '''
    edge_trace = go.Scatter(x=(), y=(), mode='lines',
                            name=legend_name,
                            line=dict(width=0.5, color=edge_color),
                            hoverinfo='none',
                            visible=visible)
    # Since plotly stores data in tuples it's more efficient for us to first build them with lists
    x_values, y_values = [], []
    for from_ep, to_ep, description in data:
        posn1 = node_posns[ep_node_dict[from_ep]]
        posn2 = node_posns[ep_node_dict[to_ep]]

        # Add an edge
        x_values.extend([posn1[0], posn2[0], None])
        y_values.extend([posn1[1], posn2[1], None])

        # Add mouseover text to the 'to' nodes
        if to_text is not None:
            mouseover_texts[ep_node_dict[to_ep]] += \
                '<br>' + to_text.format(from_ep=from_ep) + f'; {description}'

    # Add mouseover to the 'from' nodes (in a separate loop so incoming continuity is listed
    # before outgoing continuity within a given episode)
    if from_text is not None:
        for from_ep, to_ep, description in data:
            mouseover_texts[ep_node_dict[from_ep]] += \
                '<br>' + from_text.format(to_ep=to_ep) + f'; {description}'

    edge_trace['x'], edge_trace['y'] = tuple(x_values), tuple(y_values)

    return edge_trace


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(dest='show_data_module', type=str,
                        help="The python module to import show data from.")
    parser.add_argument('--add-spoiler-free-plot', action='store_true', default=False,
                        dest="add_spoiler_free_plot",
                        help="Additionally create a plot with no mouseover text" \
                             + " (episode titles / connection descriptions)")
    parser.add_argument('--publish', action='store_true', dest="publish", default=False,
                        help="Publicly publish the plot to the preset plotly profile.")
    args = parser.parse_args()

    # Import show data from the given module
    show = __import__(args.show_data_module)

    print('Creating continuity plot...')

    # Add nodes for episodes to the networkx graph
    print('    Adding episode nodes...', flush=True)

    node_trace = go.Scatter(x=(), y=(),
        hoverinfo='none',
        showlegend=False,
        mode='markers',
        marker=dict(
            color=[],
            size=5,
            line=dict(width=1)),
        visible=True) # The thickness of the node's border line

    # Get the node posns arranged arranged in a semicircle
    node_posns = tuple(semicircular_positions(len(show.episodes)))
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

    plot_trace = get_continuity_edge_trace(mouseover_texts, node_posns, ep_node_dict,
                                           show.plot_threads,
                                           legend_name='Plot Threads', edge_color='black',
                                           visible='legendonly',
                                           to_text='Continues plot of ep {from_ep}')

    callbacks_trace = get_continuity_edge_trace(mouseover_texts, node_posns, ep_node_dict,
                                                show.callbacks,
                                                legend_name='Callbacks', edge_color='orange',
                                                visible='legendonly',
                                                from_text='Callbacks ep {to_ep}')

    foreshadowing_trace = get_continuity_edge_trace(mouseover_texts, node_posns, ep_node_dict,
                                                    show.foreshadowing,
                                                    legend_name='Foreshadowing', edge_color='blue',
                                                    to_text='Foreshadowed by ep {from_ep}',
                                                    from_text='Foreshadows ep {to_ep}')

    # Prepare the figure layout for the plots
    fig_layout = go.Layout(
        title=dict(text=f'<br><b>Continuity in {show.title}</b>',
                   font=dict(color='black', size=16), x=0.5),
        showlegend=True,
        legend=dict(x=0.9, y=0.95, itemdoubleclick=False),
        # If hovermode is set to 'closest', it picks any node close enough to the mouse's position
        # If set to e.g. 'x', picks the node (any distance away) which is closest to the mouse's x
        # position.
        hovermode='closest',
        dragmode='pan', # Default mouse mode
        margin=dict(b=5, l=5, r=5, t=40, pad=0),
        annotations=[ dict(
            text="Click on legend items to show/hide them.",
            showarrow=False,
            xref="paper", yref="paper",
            x=1.0, y=1.0) ],
        plot_bgcolor='white',
        # Maintain the x-y ratio so the plot is a semicircle regardless of screen size
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False,
                   scaleanchor='x', scaleratio=1, range=[-0.05, 1.05]))

    if args.add_spoiler_free_plot:
        print('Plotting the spoiler-free figure with Plotly...', flush=True)

        spoiler_free_fig = go.Figure(
                data=[node_trace, plot_trace, callbacks_trace, foreshadowing_trace],
                layout=fig_layout)

        no_spoilers_filename = args.show_data_module + '_no_spoilers_continuity_graph'
        if not args.publish:
            plotly.offline.plot(spoiler_free_fig, filename=no_spoilers_filename + '.html',
                                show_link=False, auto_open=True)
        else:
            chart_studio.plotly.plot(spoiler_free_fig, filename=no_spoilers_filename, sharing='public')

    print('Plotting the figure with Plotly...', flush=True)
    # Add the node mouseover data now that we're done with the spoiler-free plot
    # Add node mouseover text to the node trace, now that we're done updating them with edge data
    node_trace.hoverinfo = 'text'
    node_trace.hoverlabel = dict(align='left')
    node_trace.hovertext = tuple(text for text in mouseover_texts)
    # Modify the helper text for the spoiler version to mention the node mouseovers
    fig_layout.annotations[0]['text'] = \
            "Hover over nodes to see details.<br>Click on legend items to show/hide them."

    fig = go.Figure(data=[node_trace, plot_trace, callbacks_trace, foreshadowing_trace],
                    layout=fig_layout)

    filename = args.show_data_module + '_continuity_graph'
    if not args.publish:
        plotly.offline.plot(fig, filename=filename + '.html', show_link=False, auto_open=True)
    else:
        chart_studio.plotly.plot(fig, filename=filename, sharing='public')

    print('Done.')

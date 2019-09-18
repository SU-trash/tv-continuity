#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-

# TODO: Modify mouseover tips when foreshadowing/callbacks/plot threads traces are disabled
# TODO: Hide or fade to background edges that don't touch the node currently being hovered over
# TODO: See if PLotly ever allows left-aligning mouseover text (even when mouseover appears to the
#       left of a node
# TODO: Add a way to view a single season at a time (with nodes redistributed into a new semicircle)
#       Alternatively, just make some separate per-season graphs
# TODO: Prevent episode nodes from being hidden by plotly on legend double-click (hides all but one
#       trace, but also hides traces that were hidden from the legend)
# TODO: See if any use for plotly's 'legendgroup' can be found in future extensions of this
# TODO: Fix figure starting too zoomed out, resulting in large initial top margin

print 'Loading libraries...'

import sys
sys.stdout.flush()

import argparse
import math
import numpy as np

import plotly
import plotly.graph_objs as go

import steven_universe as show

BASE_FILE_NAME = 'SU_continuity_graph'

def semicircular_positions(N):
    '''Return a list of n position tuples forming a semicircle on the unit circle. First and last
    positions are always (-1, 0) and (1, 0).'''
    # Edge case to avoid dividing by 0
    if N == 1:
        return [(-1.0, 0.0)]

    posns = []
    for i in range(N):
        # Calculate the angle of this position in radians
        theta = (math.pi * (N - 1 - i)) / (N - 1) # Float division
        posns.append((math.cos(theta), math.sin(theta)))
    return posns


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--add-spoiler-free-plot', action='store_true', default=False,
                        dest="add_spoiler_free_plot",
                        help="Additionally create a plot with no mouseover text" \
                             + " (episode titles / connection descriptions)")
    parser.add_argument('--publish', action='store_true', dest="publish", default=False,
                        help="Publicly publish the plot to the preset plotly profile.")
    args = parser.parse_args()

    print 'Creating continuity plot...'

    # Add nodes for episodes to the networkx graph
    print '    Adding episode nodes...'
    sys.stdout.flush()

    node_trace = go.Scatter(x=[], y=[],
        hoverinfo='none',
        showlegend=False, # Don't show nodes in legend
        mode='markers',
        marker=dict(
            color=[],
            size=5,
            line=dict(width=1))) # The thickness of the node's border line

    # Get the node posns arranged arranged in a semicircle
    node_posns = semicircular_positions(show.num_episodes)
    node_trace['x'] = tuple([node_posns[i][0] for i in range(show.num_episodes)])
    node_trace['y'] = tuple([node_posns[i][1] for i in range(show.num_episodes)])

    # Color nodes by season
    node_colors = []
    for season_num, season_info in show.seasons.items():
        # Use episode_indices dict to take double-length eps into account
        start = show.episode_indices[season_info['start']]
        if 'end' in season_info:
            end = show.episode_indices[season_info['end']]
        else: # If the season hasn't yet ended:
            end = show.num_episodes
        num_eps = end - start + 1
        node_colors.extend(num_eps*[season_info['color']])
    node_trace['marker']['color'] = tuple(node_colors)

    # Create mouseover text for each node. We'll update the mouseover text for each episode based
    # on its edge connections
    mouseover_texts = ["<b>Ep " + str(ep_num) + ': ' + ep_title + '</b>'
                       for ep_num, ep_title in show.episodes.items()]

    print '    Adding edges...'
    sys.stdout.flush()

    # Add black edges for plot threads
    plot_trace = go.Scatter(x=[], y=[],
                            name='Plot Threads',
                            line=dict(width=0.5, color='black'),
                            hoverinfo='none',
                            mode='lines')
    # Since plotly stores data in tuples it's more efficient for us to first build them with lists
    x_values, y_values = [], []
    for source_ep, target_ep, description in show.plot_threads:
        posn1 = node_posns[show.episode_indices[source_ep]]
        posn2 = node_posns[show.episode_indices[target_ep]]
        x_values.extend([posn1[0], posn2[0], None])
        y_values.extend([posn1[1], posn2[1], None])

        # Add description of plot threads an episode picks up to its mouseover text
        mouseover_texts[show.episode_indices[target_ep]] += \
                '<br>Continues plot of ep {0}; {1}'.format(source_ep, description)
    plot_trace['x'], plot_trace['y'] = tuple(x_values), tuple(y_values)

    # Add orange edges for callbacks
    callbacks_trace = go.Scatter(x=[], y=[],
                                 name='Callbacks',
                                 line=dict(width=0.5, color='orange'),
                                 hoverinfo='none',
                                 mode='lines')
    # Since plotly stores data in tuples it's more efficient for us to first build them with lists
    x_values, y_values = [], []
    for source_ep, prior_ep, description in show.callbacks:
        posn1 = node_posns[show.episode_indices[source_ep]]
        posn2 = node_posns[show.episode_indices[prior_ep]]
        x_values.extend([posn1[0], posn2[0], None])
        y_values.extend([posn1[1], posn2[1], None])

        # Add description of callbacks an episode makes to its mouseover text
        mouseover_texts[show.episode_indices[source_ep]] += \
                '<br>Callbacks ep {0}; {1}'.format(prior_ep, description)
    callbacks_trace['x'], callbacks_trace['y'] = tuple(x_values), tuple(y_values)

    # Add blue edge for foreshadowing
    foreshadowing_trace = go.Scatter(x=[], y=[],
                                     name='Foreshadowing',
                                     line=dict(width=0.5, color='blue'),
                                     hoverinfo='none',
                                     mode='lines')
    # Since plotly stores data in tuples it's more efficient for us to first build them with lists
    x_values, y_values = [], []
    for source_ep, future_ep, description in show.foreshadowing:
        posn1 = node_posns[show.episode_indices[source_ep]]
        posn2 = node_posns[show.episode_indices[future_ep]]
        x_values.extend([posn1[0], posn2[0], None])
        y_values.extend([posn1[1], posn2[1], None])

        # Add mouseover text for foreshadowed events in an episode
        mouseover_texts[show.episode_indices[future_ep]] += \
                '<br>Foreshadowed by ep {0}; {1}'.format(source_ep, description)
    foreshadowing_trace['x'], foreshadowing_trace['y'] = tuple(x_values), tuple(y_values)
    # Add mouseover for outgoing foreshadowing to each episode (in a separate loop so foreshadowed
    # events are listed separately from outgoing foreshadowing within a given episode)
    for source_ep, future_ep, description in show.foreshadowing:
        mouseover_texts[show.episode_indices[source_ep]] += \
                '<br>Foreshadows ep {0}; {1}'.format(future_ep, description)

    # Create Network Graph
    print '    Creating the plot figure...'
    sys.stdout.flush()

    fig_layout = go.Layout(
        title='<br><b>Continuity in Steven Universe</b>',
        titlefont=dict(size=16),
        showlegend=True,
        legend=dict(x = 0.9, y = 0.95),
        hovermode='closest',
        dragmode='pan', # Default mouse mode
        margin=dict(b=5,l=5,r=5,t=40, pad=0),
        annotations=[ dict(
            text="Click on legend items to show/hide them.",
            showarrow=False,
            xref="paper", yref="paper",
            x=1.0, y=1.0) ],
        # Maintain the x-y ratio so the plot is a semicircle regardless of screen size
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False,
                   scaleanchor='x', scaleratio=1))

    if args.add_spoiler_free_plot:
        print 'Plotting the spoiler-free figure with Plotly...'
        sys.stdout.flush()
        spoiler_free_fig = go.Figure(
                data=[node_trace, plot_trace, callbacks_trace, foreshadowing_trace],
                layout=fig_layout)

        no_spoilers_file_name = BASE_FILE_NAME + '_no_spoilers'
        if not args.publish:
            plotly.offline.plot(spoiler_free_fig, filename=no_spoilers_file_name + '.html',
                                show_link=False, auto_open=True)
        else:
            plotly.plotly.plot(spoiler_free_fig, filename=no_spoilers_file_name, sharing='public')

    print 'Plotting the figure with Plotly...'
    sys.stdout.flush()

    # Add the node mouseover data now that we're done with the spoiler-free plot
    # Add node mouseover text to the node trace, now that we're done updating them with edge data
    node_trace.hoverinfo = 'text'
    node_trace.hovertext = tuple([text for text in mouseover_texts])
    # Modify the helper text for the spoiler version to mention the node mouseovers
    fig_layout.annotations[0]['text'] = \
            "Hover over nodes to see details.<br>Click on legend items to show/hide them."

    fig = go.Figure(data=[node_trace, plot_trace, callbacks_trace, foreshadowing_trace],
                    layout=fig_layout)

    if not args.publish:
        plotly.offline.plot(fig, filename=BASE_FILE_NAME + '.html', show_link=False, auto_open=True)
    else:
        plotly.plotly.plot(fig, filename=BASE_FILE_NAME, sharing='public')

    print 'Done.'

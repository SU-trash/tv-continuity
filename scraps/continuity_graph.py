from collections import OrderedDict
import matplotlib.pyplot as plt
import numpy as np

import networkx as nx # Helper for plotting graphs in matplotlib

import steven_universe as show

# When mousing over episode node, list all connections to that episode, below the episode title
# TODO: Move away from networkx
# TODO: Add more data
# TODO: Add some easy way to distinguish seasons (coloured nodes?)
# TODO: Move to qtplot with checkboxes to show/hide plot/foreshadowing/callbacks

def semicircular_layout(G):
    """Adapted from nx.circular_layout
    Position nodes on a semi-circle. Adapted from networkx's circular_layout, and oriented
    clockwise instead of counter-clockwise
    Parameters
    ----------
    G : NetworkX graph or list of nodes
        A position will be assigned to every node in G.
    Returns
    -------
    pos : dict
        A dictionary of positions keyed by node
    """
    center = np.zeros(2) # 2 is the # of dimensions here
    paddims = 0

    if len(G) == 0:
        pos = {}
    elif len(G) == 1:
        pos = {nx.utils.arbitrary_element(G): center}
    else:
        # Discard the extra angle since it matches 0 radians.
        theta = np.linspace(start=1, stop=0, num=len(G) + 1)[:-1] * np.pi
        theta = theta.astype(np.float32)
        pos = np.column_stack([np.cos(theta), np.sin(theta),
                               np.zeros((len(G), paddims))])
        pos += center
        pos = dict(zip(G, pos))

    return pos

if __name__ == '__main__':
    G = nx.Graph()

    # Set up the plot
    fig = plt.figure(figsize=(12, 4)) # Stretch the window horizontally
    #ax = fig.add_axes((0, 0, 1, 1)) # Tighter but probably will interfere with legend
    ax = fig.add_subplot(111)
    ax.set_axis_off()
    plt.tight_layout()

    # Add nodes for each episode
    G.add_nodes_from(range(1, show.num_episodes + 1))
    # Lay the nodes out in a semicircle and keep track of their (x,y) positions
    node_posns = semicircular_layout(G)
    node_collection = nx.draw_networkx_nodes(G, pos=node_posns, ax=ax,
                                             node_size=10,
                                             node_color='black')

    # Initialize mouseover descriptions for each node
    # In addition to the episode number/title, for each episode we'll add to the description:
    #  - Plot threads it continues from older episodes
    #  - callbacks it makes to older episodes
    #  - foreshadowing for it from older episodes
    #  - foreshadowing it contains about future episodes
    node_descriptions = {}
    for ep_num in range(1, len(show.episode_titles) + 1):
        node_descriptions[ep_num] = "Ep " + str(ep_num) + ': ' + show.episode_titles[ep_num]

    # Add edges for episode relationships we're tracking
    edge_descriptions = {}
    edge_collections = []
    edge_lists = []
    def add_edges(episode_connections, format_string, **kwargs):
        '''Add the given list of edges to G in the given color.
        Args:
            episode_connections: list of tuples which have format (source_ep, target_ep, description)
            format_string: Description of the connection to be used on mouseover, formatted for a
                           call of format_string.format(...) with args {source_ep}, {target_ep}, and
                           {description}.
            **kwargs: args to pass to the call to nx.Graph.add_edge()
        '''
        if 'width' not in kwargs:
            kwargs['width'] = 2 # Override default edge thickness
        if 'alpha' not in kwargs:
            kwargs['alpha'] = 0.5 # Override default transparency

        added_edges = []
        for source_ep, target_ep, description in episode_connections:
            edge_description = format_string.format(source_ep=source_ep,
                                                    target_ep=target_ep,
                                                    description=description)

            # Networkx stores added edges undirected, starting with the lower node
            # Seriously, FUCK networkx
            source_ep, target_ep = min(source_ep, target_ep), max(source_ep, target_ep)

            G.add_edge(source_ep, target_ep)
            added_edges.append((source_ep, target_ep))
            if source_ep not in edge_descriptions:
                edge_descriptions[source_ep] = {}
            if target_ep not in edge_descriptions[source_ep]:
                edge_descriptions[source_ep][target_ep] = []
            edge_descriptions[source_ep][target_ep].append(edge_description)

        edge_collections.append(nx.draw_networkx_edges(G, pos=node_posns, ax=ax,
                                                       edgelist=added_edges,
                                                       arrows=False,
                                                       **kwargs))
        edge_lists.append(added_edges)

    # Add black edges for direct plot threads
    add_edges(show.plot_threads,
              format_string="Ep {target_ep} continues plot of ep {source_ep}: {description}",
              label='plot',
              edge_color='black')
    for ep1, ep2, description in show.plot_threads:
        node_descriptions[ep2] += "\ncontinues plot of ep {0}: {1}".format(ep1, description)

    # Add orange edges for continuity/callbacks
    add_edges(show.callbacks,
              format_string="Ep {source_ep} callbacks ep {target_ep}: {description}",
              label='callback',
              edge_color='orange')
    for ep1, ep2, description in show.callbacks:
        node_descriptions[ep1] += "\ncallbacks ep {0}: {1}".format(ep2, description)

    # Add blue edges for foreshadowing (plot last so they show up on top)
    add_edges(show.foreshadowing,
              format_string="Ep {source_ep} foreshadows ep {target_ep}: {description}",
              label='foreshadowing',
              edge_color='blue')
    for ep1, ep2, description in show.foreshadowing:
        node_descriptions[ep2] += "\nforeshadowed by ep {0}: {1}".format(ep1, description)
    for ep1, ep2, description in show.foreshadowing:
        node_descriptions[ep1] += "\nforeshadows ep {0}: {1}".format(ep2, description)

    # Add legend for edge types
    # I want to plot foreshadowing last so it shows up better over other edges, but I also think
    # plot | foreshadowing | callbacks feels like a logical ordering for the legend, so rearrange
    # it now
    legend_label_order = {'plot': 1, 'foreshadowing': 2, 'callback': 3}
    handles, labels = ax.get_legend_handles_labels()
    hl = sorted(zip(handles, labels),
                key=lambda x:legend_label_order[x[1]])
    handles2, labels2 = zip(*hl)
    #ax.legend(handles2, labels2)

    # Add plot title
    ax.set_title('Continuity in ' + show.title)

    # Disable xy coordinate display in matplotlib toolbar
    ax.format_coord = lambda x, y: ""

    # Add mouseover info to nodes/edges
    # Code shamelessly stolen from https://stackoverflow.com/a/47166787
    # Note: annotation box properties can be modified at runtime
    #       with e.g. annot.get_bbox_patch().set_facecolor(0.75)
    # textcoords="offset points"
    annot_left = ax.annotate("", xy=(0,0), xytext=(0,-0.05), textcoords="axes fraction",
                             bbox=dict(boxstyle="square", fc="pink", alpha=0.75),
                             arrowprops=dict(arrowstyle="->"))
    annot_left.set_visible(False)
    annot_right = ax.annotate("", xy=(0,0), xytext=(0.35,-0.05), textcoords="axes fraction",
                              bbox=dict(boxstyle="square", fc="pink", alpha=0.75),
                              arrowprops=dict(arrowstyle="->"))
    annot_right.set_visible(False)

    # We now need the node_posns in the format returned by node_collection
    _node_posns = node_collection.get_offsets()
    def update_annot_node(node_idx, mouse_pos):
        if mouse_pos[0] > 0:
            annot = annot_left
            other_annot = annot_right
        else:
            annot = annot_right
            other_annot = annot_left
        annot.xy = _node_posns[node_idx] # Point to the node not the mouse to avoid confusion
        ep_num = node_idx + 1
        annot.set_text(node_descriptions[ep_num])
        annot.set_visible(True)
        other_annot.set_visible(False)

    def update_annot_edges(edges, mouse_pos):
        if mouse_pos[0] > 0:
            annot = annot_left
            other_annot = annot_right
        else:
            annot = annot_right
            other_annot = annot_left
        annot.xy = mouse_pos
        text = "\n".join("\n".join(edge_descriptions[s][t]) for s, t in edges)
        annot.set_text(text)
        annot.set_visible(True)
        other_annot.set_visible(False)

    def hover(event):
        if event.inaxes == ax:
            on_nodes, nodes_info = node_collection.contains(event)
            if on_nodes:
                matching_node = nodes_info["ind"][0] # We'll only tooltip one node at a time
                update_annot_node(matching_node, mouse_pos=(event.xdata, event.ydata))
                fig.canvas.draw_idle()
            else:
                matching_edges = set()
                for edge_collection, edge_list in zip(edge_collections, edge_lists):
                    _, edges_info = edge_collection.contains(event)
                    [matching_edges.add(edge_list[i]) for i in edges_info['ind']]
                if matching_edges:
                    update_annot_edges(matching_edges, mouse_pos=(event.xdata, event.ydata))
                    fig.canvas.draw_idle()
                elif annot_left.get_visible() or annot_right.get_visible():
                    # If we're no longer on any object hide the mouseover info
                    annot_right.set_visible(False)
                    annot_left.set_visible(False)
                    fig.canvas.draw_idle()
    fig.canvas.mpl_connect("motion_notify_event", hover)

    plt.draw_if_interactive()
    plt.show()

    #plotly.offline.plot_mpl(fig, filename='SU_continuity_graph.html')

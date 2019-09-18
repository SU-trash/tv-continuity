import numpy as np

# Matplotlib
import matplotlib.pyplot as plt
from matplotlib import collections as mc # For Line Collections

# Plotly
import plotly.plotly
import plotly.tools as tls

if __name__ == '__main__':
    # Creating the matplotlib graph..
    mpl_fig = plt.figure(figsize=(12, 4))
    ax = mpl_fig.add_subplot(111)
    ax.set_axis_off()
    plt.tight_layout()

    ## Generating the data..
    x = np.linspace(np.pi, 3*np.pi, 100)
    sinx = np.sin(x)
    logx = np.log(x)

    ## Test adding some matplotlib lines to the graph:
    # Plotly doesn't like just adding a MPL Line Collection - investigate using networkx

    # Add legend - THIS BREAKS THE MATPLOTLIB -> PLOTLY CONVERSION
    #handles, labels = ax.get_legend_handles_labels()
    #ax.legend(handles, labels)

    # Plotting
    ax.plot(x, sinx)
    ax.set_title('A Sine Curve')

    # Converting to Plotly
    #plotly_fig = tls.mpl_to_plotly(mpl_fig)
    plotly.offline.plot_mpl(mpl_fig, filename='plotly_example_plot.html')

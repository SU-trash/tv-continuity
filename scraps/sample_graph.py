from matplotlib import pyplot as plt
from matplotlib.collections import LineCollection
import numpy as np

if __name__ == '__main__':
    points = np.random.randint(0, 100, (100, 2))
    edges = np.random.randint(0, 100, (200, 2))

    # Config
    lc = LineCollection(points[edges])

    fig = plt.figure(figsize=(12, 4)) # Stretch the window horizontally
    #ax = fig.add_axes((0, 0, 1, 1)) # Tighter but probably will interfere with legend
    ax = fig.add_subplot(111)
    ax.set_axis_off()
    plt.tight_layout()

    ax.add_collection(lc)
    plt.xlim(points[:,0].min(), points[:,0].max())
    plt.ylim(points[:,1].min(), points[:,1].max())
    plt.plot(points[:,0], points[:,1], 'ro')
    plt.show()

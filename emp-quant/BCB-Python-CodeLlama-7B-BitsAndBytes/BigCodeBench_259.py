
import matplotlib.pyplot as plt
import numpy as np

def task_func(ax, num_points):
    if not isinstance(ax, plt.Axes):
        raise ValueError("Input ax must be a matplotlib.axes._axes.Axes object.")
    if num_points < 0:
        raise ValueError("Number of points must be a positive integer.")

    # Generate random points on the polar diagram
    theta = np.random.uniform(0, 2 * np.pi, num_points)
    r = np.random.uniform(0, 1, num_points)
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    # Plot the points
    ax.scatter(x, y, c='red')

    # Set the radial ticks
    ax.set_rmax(1)
    ax.set_rticks(np.arange(0, 1.1, 0.1))
    ax.set_rlabel_position(-22.5)

    return ax
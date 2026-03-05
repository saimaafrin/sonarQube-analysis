
import matplotlib.pyplot as plt
import numpy as np

def task_func(ax, num_points):
    if not isinstance(ax, plt.Axes):
        raise ValueError("Input ax must be a matplotlib.axes._axes.Axes object")
    if num_points < 0:
        raise ValueError("Number of points must be a positive integer")

    # Generate random points on the polar diagram
    theta = np.random.uniform(0, 2 * np.pi, num_points)
    r = np.random.uniform(0, 1, num_points)

    # Plot the points on the polar diagram
    ax.plot(theta, r, 'o-')

    # Set the radial ticks based on the number of points divided by 10 degrees
    ax.set_rmax(1)
    ax.set_rticks(np.arange(0, 1.1, 0.1))
    ax.set_rlabel_position(-22.5)

    return ax
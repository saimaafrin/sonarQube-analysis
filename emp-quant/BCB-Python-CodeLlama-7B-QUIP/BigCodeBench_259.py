
import matplotlib
import numpy as np
def task_func(ax, num_points):
    if not isinstance(ax, matplotlib.axes.Axes):
        raise ValueError("Input ax must be an Axes object")
    if num_points < 0:
        raise ValueError("num_points must be a positive integer")
    # Generate random points on the polar diagram
    theta = np.linspace(0, 2 * np.pi, num_points)
    r = np.random.rand(num_points)
    # Plot the points on the polar diagram
    ax.scatter(theta, r)
    # Set the radial ticks based on the number of points divided by 10 degrees
    ax.set_xticks(np.linspace(0, 2 * np.pi, num_points // 10))
    return ax
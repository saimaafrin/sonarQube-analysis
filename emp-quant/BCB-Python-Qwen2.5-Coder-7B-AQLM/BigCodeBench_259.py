
import matplotlib
import numpy as np

def task_func(ax, num_points):
    if not isinstance(ax, matplotlib.axes._axes.Axes):
        raise ValueError("The input ax must be a matplotlib Axes object.")
    if num_points < 0:
        raise ValueError("The number of points cannot be negative.")
    
    # Generate random points
    theta = np.random.uniform(0, 2 * np.pi, num_points)
    r = np.random.uniform(0, 1, num_points)
    
    # Plot the points
    ax.scatter(theta, r)
    
    # Set radial ticks
    num_ticks = num_points // 10
    if num_ticks > 0:
        ax.set_rticks(np.linspace(0, 1, num_ticks + 1))
    
    return ax
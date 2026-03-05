
import matplotlib.pyplot as plt
import numpy as np

def task_func(ax, num_points):
    if not isinstance(ax, plt.Axes):
        raise ValueError("Input ax must be a matplotlib.axes._axes.Axes object.")
    if num_points < 0:
        raise ValueError("num_points cannot be a negative number.")
    
    # Generate random angles and radii
    angles = np.random.uniform(0, 2 * np.pi, num_points)
    radii = np.random.uniform(0, 1, num_points)
    
    # Plot the points
    ax.scatter(angles, radii)
    
    # Set radial ticks
    num_ticks = num_points // 10
    if num_ticks == 0:
        num_ticks = 1
    ax.set_rticks(np.linspace(0, 1, num_ticks + 1))
    
    return ax
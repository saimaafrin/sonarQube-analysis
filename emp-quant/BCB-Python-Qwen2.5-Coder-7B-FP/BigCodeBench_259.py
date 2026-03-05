import matplotlib.pyplot as plt
import numpy as np
def task_func(ax, num_points):
    """
    Plots 'num_points' random points on the polar diagram represented by 'ax'.
    The radial ticks on the plot are positioned based on the number of points divided by 10 degrees.
    
    Parameters:
    ax (matplotlib.axes._axes.Axes): The Axes object to plot on.
    num_points (int): The number of random points to plot.
    
    Returns:
    matplotlib.axes._axes.Axes: The modified Axes object with plotted points.
    
    Raises:
    ValueError: If 'ax' is not an Axes object or if 'num_points' is a negative number.
    """
    if not isinstance(ax, plt.Axes):
        raise ValueError("The input ax must be an Axes object.")
    if num_points < 0:
        raise ValueError("The number of points cannot be negative.")
    
    # Generate random angles and radii
    angles = np.random.uniform(0, 2 * np.pi, num_points)
    radii = np.random.uniform(0, 1, num_points)
    
    # Plot the points
    ax.scatter(angles, radii)
    
    # Set radial ticks
    num_ticks = int(num_points / 10)
    if num_ticks > 0:
        ax.set_rticks(np.linspace(0, 1, num_ticks + 1))
    
    return ax
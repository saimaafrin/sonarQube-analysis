import matplotlib
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
    # Check if 'ax' is an Axes object
    if not isinstance(ax, matplotlib.axes._axes.Axes):
        raise ValueError("The input 'ax' must be a matplotlib.axes._axes.Axes object.")
    
    # Check if 'num_points' is a non-negative integer
    if not isinstance(num_points, int) or num_points < 0:
        raise ValueError("The input 'num_points' must be a non-negative integer.")
    
    # Generate random angles and radii
    angles = np.random.uniform(0, 2 * np.pi, num_points)
    radii = np.random.uniform(0, 1, num_points)
    
    # Plot the points on the polar plot
    ax.plot(angles, radii, 'o')
    
    # Set radial ticks based on the number of points
    tick_interval = max(1, num_points // 10)
    ax.set_rticks(np.arange(0, 1.1, tick_interval))
    
    return ax
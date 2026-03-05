
import matplotlib
import numpy as np

def task_func(ax, num_points):
    """
    Plots "num_points" random points on the polar diagram represented by "ax."
    The radial ticks on the plot are positioned based on the number of points divided by 10 degrees.
    
    Parameters:
    ax (matplotlib.axes._subplots.AxesSubplot): The Axes object to plot on.
    num_points (int): The number of random points to plot.
    
    Returns:
    matplotlib.axes._axes.Axes: The modified Axes object with plotted points.
    
    Raises:
    ValueError: If ax is not an instance of matplotlib.axes._subplots.AxesSubplot.
    ValueError: If num_points is a negative number.
    """
    if not isinstance(ax, matplotlib.axes._subplots.AxesSubplot):
        raise ValueError("ax must be an instance of matplotlib.axes._subplots.AxesSubplot")
    
    if num_points < 0:
        raise ValueError("num_points must be a non-negative number")
    
    # Generate random points
    theta = np.random.uniform(0, 2 * np.pi, num_points)
    radius = np.random.rand(num_points)
    
    # Plot the points
    ax.scatter(theta, radius, c='red', marker='o')
    
    # Set the radial ticks
    ax.set_xticks(np.arange(0, 360, 360 / num_points))
    
    return ax
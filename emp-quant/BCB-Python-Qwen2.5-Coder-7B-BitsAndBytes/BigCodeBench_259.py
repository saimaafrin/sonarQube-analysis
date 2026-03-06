
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
    ValueError: If 'ax' is not an instance of matplotlib.axes._axes.Axes.
    ValueError: If 'num_points' is a negative number.
    """

    # Check if ax is an instance of matplotlib.axes._axes.Axes
    if not isinstance(ax, plt.Axes):
        raise ValueError("This function will raise a ValueError if the input ax is not and Axes.")

    # Check if num_points is a negative number
    if num_points < 0:
        raise ValueError("This function will raise a ValueError if it is use the negative number as num_points.")

    # Generate random angles and radii
    theta = np.random.uniform(0, 2 * np.pi, num_points)
    r = np.random.rand(num_points)

    # Plot the points
    ax.scatter(theta, r)

    # Set radial ticks
    tick_interval = max(1, num_points // 10)
    ax.set_rticks(np.arange(0, 1.1, tick_interval))

    return ax
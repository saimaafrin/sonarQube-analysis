import matplotlib.pyplot as plt
import numpy as np
def task_func(ax, num_points):
    """
    Plots "num_points" random points on the polar diagram represented by "ax."
    The radial ticks on the plot are positioned based on the number of points divided by 10 degrees.
    The function should raise the exception for:
        - This function will raise a ValueError if the input ax is not and Axes.
        - This function will raise a ValueError if it is use the negative number as num_points.
    The function should output with:
        - matplotlib.axes._axes.Axes: The modified Axes object with plotted points.
    """
    if not isinstance(ax, plt.Axes):
        raise ValueError("Input ax must be an Axes object.")
    if num_points < 0:
        raise ValueError("Number of points must be a positive integer.")

    # Generate random points on the polar diagram
    theta = np.linspace(0, 2 * np.pi, num_points)
    r = np.random.uniform(0.5, 1, num_points)
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    # Plot the points
    ax.plot(x, y, "o-")

    # Set the radial ticks
    ax.set_rmax(1.1 * max(r))
    ax.set_rticks(np.linspace(0, 1.1 * max(r), 11))
    ax.set_rlabel_position(-22.5)

    return ax
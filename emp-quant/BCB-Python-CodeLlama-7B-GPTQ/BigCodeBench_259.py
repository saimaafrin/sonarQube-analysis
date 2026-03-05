import matplotlib
import numpy as np
def task_func(ax, num_points):
    """
    Plots "num_points" random points on the polar diagram represented by "ax." The radial ticks on the plot are positioned based on the number of points divided by 10 degrees.
    The function should raise the exception for:
        - This function will raise a ValueError if the input ax is not and Axes.
        - This function will raise a ValueError if it is use the negative number as num_points.
    The function should output with:
        - matplotlib.axes._axes.Axes: The modified Axes object with plotted points.
    """
    if not isinstance(ax, matplotlib.axes.Axes):
        raise ValueError("The input ax is not an Axes object.")
    if num_points < 0:
        raise ValueError("The number of points must be a positive integer.")

    # Generate random points on the polar diagram
    theta = np.linspace(0, 2 * np.pi, num_points)
    r = np.random.uniform(0, 1, num_points)

    # Plot the points on the polar diagram
    ax.plot(theta, r, "o")

    # Set the radial ticks
    ax.set_xticks(np.linspace(0, 2 * np.pi, num_points // 10))
    ax.set_yticks(np.linspace(0, 1, num_points // 10))

    return ax
ax = matplotlib.pyplot.subplot(111, polar=True)
import matplotlib
import numpy as np
def task_func(ax, num_points):
    """
    Plots "num_points" random points on the polar diagram represented by "ax."
    The radial ticks on the plot are positioned based on the number of points divided by 10 degrees.

    Parameters:
    ax (matplotlib.axes._axes.Axes): The Axes object for the polar plot.
    num_points (int): The number of random points to generate and plot.

    Returns:
    matplotlib.axes._axes.Axes: The modified Axes object with plotted points.

    Raises:
    - This function will raise a ValueError if the input ax is not and Axes.
    - This function will raise a ValueError if it is use the negative number as num_points.

    Requirements:
    - matplotlib
    - numpy

    Example:
    >>> np.random.seed(0)
    >>> fig = plt.figure()
    >>> ax = fig.add_subplot(111, polar=True)
    >>> ax = task_func(ax, 100)
    >>> ax.get_rlabel_position()
    10.0
    >>> plt.close()
    """
    if not isinstance(ax, matplotlib.axes.Axes):
        raise ValueError("ax must be an Axes object.")
    if num_points < 0:
        raise ValueError("num_points must be a positive number.")

    # Generate random points on the polar diagram.
    theta = np.random.rand(num_points) * 2 * np.pi
    r = np.random.rand(num_points)

    # Plot the points.
    ax.plot(theta, r, "o")

    # Set the radial ticks.
    ax.set_rticks([0.5, 1, 1.5, 2])

    # Set the radial tick labels.
    ax.set_rlabel_position(10)

    return ax
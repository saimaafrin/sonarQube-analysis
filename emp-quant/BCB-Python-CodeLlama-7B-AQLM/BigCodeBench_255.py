import matplotlib
import numpy as np
FUNCTIONS = [np.sin, np.cos, np.tan]
def task_func(ax, func_index):
    """
    Draw a mathematical function (sine, cosine, or tangent) on a polar diagram 'ax'.
    The radial ticks are placed at a position corresponding to the index of the function multiplied by 45 degrees.

    Parameters:
    ax (matplotlib.axes._axes.Axes): The ax to plot on.
    func_index (int): The index of the function in the FUNCTIONS list (0 for sine, 1 for cosine, 2 for tangent).

    Returns:
    matplotlib.axes._axes.Axes: The modified ax with the plotted function.
    
    Raises:
    - This function will raise a ValueError if the input ax is not and Axes.
    
    Requirements:
    - matplotlib
    - numpy

    Example:
    >>> import matplotlib.pyplot as plt
    >>> fig = plt.figure()
    >>> ax = fig.add_subplot(111, polar=True)
    >>> ax_up = task_func(ax, 1)
    <class 'matplotlib.projections.polar.PolarAxes'>
    >>> ax_up.lines[0].get_ydata()[0]
    1.0
    >>> plt.close()
    """
    if not isinstance(ax, matplotlib.axes.Axes):
        raise ValueError("ax must be an Axes")

    # Get the function
    func = FUNCTIONS[func_index]

    # Get the number of points
    n = 100

    # Get the angle
    theta = np.linspace(0, 2*np.pi, n)

    # Get the radius
    r = func(theta)

    # Plot the function
    ax.plot(theta, r)

    # Set the radial ticks
    ax.set_rgrids(np.linspace(0, 1, n), angle=np.linspace(0, 2*np.pi, n))

    # Return the ax
    return ax
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
def task_func(func, x_range=(-2, 2), num_points=1000):
    """
    Calculates and plots both a given function and its cumulative integral over a specified range, using a linearly spaced range of x-values.

    Parameters
    ----------
    func : function
        The function to be plotted.
    x_range : tuple, optional
        The range of x-values to be used for the plot. Default is (-2, 2).
    num_points : int, optional
        The number of points to be used for the plot. Default is 1000.

    Returns
    -------
    matplotlib.axes.Axes
        The Axes object containing the plots of the function and its integral.
    """
    # Generate a linearly spaced range of x-values
    x = np.linspace(x_range[0], x_range[1], num_points)

    # Evaluate the function and its integral at each x-value
    y = func(x)
    y_int = integrate.cumulative_trapezoid(y, x)

    # Create a figure and axis object
    fig, ax = plt.subplots()

    # Plot the function and its integral
    ax.plot(x, y, label=f'{func.__name__}')
    ax.plot(x, y_int, label=f'{func.__name__} integral')

    # Add a legend and labels for the x and y axes
    ax.legend()
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    return ax
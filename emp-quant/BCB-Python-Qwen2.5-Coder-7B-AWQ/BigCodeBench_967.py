import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
def task_func(func, x_range=(-2, 2), num_points=1000):
    """
    Calculates and plots both a given function and its cumulative integral over a specified range.

    Parameters:
    func (callable): The function to be plotted.
    x_range (tuple): The range of x-values as a tuple (start, end).
    num_points (int): The number of points to use for the x-axis.

    Returns:
    matplotlib.axes.Axes: The Axes object containing the plots of the function and its integral.
    """
    # Generate linearly spaced x values
    x = np.linspace(x_range[0], x_range[1], num_points)
    
    # Calculate y values for the function
    y = func(x)
    
    # Calculate the cumulative integral of the function
    integral, _ = integrate.cumtrapz(y, x, initial=0)
    
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Plot the original function
    ax.plot(x, y, label=f'f(x) = {func.__name__}')
    
    # Plot the cumulative integral
    ax.plot(x, integral, label=f'Integral of f(x)')
    
    # Set labels and legend
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()
    
    # Show the plot
    plt.show()
    
    return ax
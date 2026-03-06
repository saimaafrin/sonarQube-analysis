
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def task_func(func, x_range=(-2, 2), num_points=1000):
    """
    Plots a given function and its cumulative integral over a specified range.

    Parameters:
    func (callable): The function to plot.
    x_range (tuple): A tuple (start, end) defining the range of x values.
    num_points (int): Number of points to use for plotting.

    Returns:
    matplotlib.axes.Axes: The Axes object containing the plots.
    """
    # Generate linearly spaced x values
    x = np.linspace(x_range[0], x_range[1], num_points)
    
    # Compute y values for the function
    y = func(x)
    
    # Compute the cumulative integral of the function
    cum_integral, _ = integrate.cumtrapz(y, x, initial=0)
    
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Plot the original function
    ax.plot(x, y, label=f'f(x) = {func.__name__}')
    
    # Plot the cumulative integral
    ax.plot(x, cum_integral, label='Cumulative Integral')
    
    # Add legend, labels, and title
    ax.legend()
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title(f'Plot of {func.__name__} and its Cumulative Integral')
    
    return ax
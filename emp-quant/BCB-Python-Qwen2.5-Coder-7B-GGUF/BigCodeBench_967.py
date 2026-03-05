
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def task_func(func, x_range=(-2, 2), num_points=1000):
    """
    Calculates and plots both a given function and its cumulative integral over a specified range.
    
    Parameters:
    func (callable): The function to be plotted.
    x_range (tuple): The range of x-values as a tuple (start, end).
    num_points (int): The number of points to use for the x-values.
    
    Returns:
    matplotlib.axes.Axes: The Axes object containing the plots of the function and its integral.
    """
    # Generate linearly spaced x values
    x = np.linspace(x_range[0], x_range[1], num_points)
    
    # Calculate the function values
    y = func(x)
    
    # Calculate the cumulative integral
    integral, _ = integrate.cumtrapz(y, x, initial=0)
    
    # Create the plot
    fig, ax = plt.subplots()
    ax.plot(x, y, label=f'Function: {func.__name__}')
    ax.plot(x, integral, label='Cumulative Integral')
    
    # Add labels and legend
    ax.set_xlabel(f'x (range: {x_range[0]} to {x_range[1]})')
    ax.set_ylabel(f'y ({func.__name__} and integral)')
    ax.legend()
    
    # Show the plot
    plt.show()
    
    return ax
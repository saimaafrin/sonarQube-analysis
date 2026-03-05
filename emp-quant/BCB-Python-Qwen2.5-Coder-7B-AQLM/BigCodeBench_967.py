
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def task_func(func, x_range=(-2, 2), num_points=1000):
    """
    Calculates and plots both a given function and its cumulative integral over a specified range.
    
    Parameters:
    func (callable): The function to plot.
    x_range (tuple): The range of x-values as a tuple (start, end).
    num_points (int): The number of points to use for the x-range.
    
    Returns:
    matplotlib.axes.Axes: The Axes object containing the plots of the function and its integral.
    """
    # Generate the x values
    x = np.linspace(x_range[0], x_range[1], num_points)
    
    # Calculate the y values for the function
    y = func(x)
    
    # Calculate the cumulative integral
    integral, _ = integrate.cumtrapz(y, x, initial=0)
    
    # Plot the function and its integral
    fig, ax = plt.subplots()
    ax.plot(x, y, label=f'{func.__name__}')
    ax.plot(x, integral, label=f'Integral of {func.__name__}')
    
    # Add labels and legend
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()
    
    return ax
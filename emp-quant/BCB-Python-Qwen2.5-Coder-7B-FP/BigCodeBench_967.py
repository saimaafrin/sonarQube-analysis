import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
def task_func(func, x_range=(-2, 2), num_points=1000):
    """
    Calculates and plots both a given function and its cumulative integral over a specified range.
    
    Parameters:
    - func: The function to be plotted and integrated.
    - x_range: A tuple (start, end) defining the range of x values.
    - num_points: The number of points to use for the x range.
    
    Returns:
    - matplotlib.axes.Axes: The Axes object containing the plots of the function and its integral.
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
    ax.plot(x, y, label=f'Function: {func.__name__}')
    
    # Plot the cumulative integral
    ax.plot(x, integral, label=f'Integral of {func.__name__}')
    
    # Set labels and legend
    ax.set_xlabel(f'x (range: {x_range[0]} to {x_range[1]})')
    ax.set_ylabel('y')
    ax.legend()
    
    # Show the plot
    plt.show()
    
    return ax

import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def task_func(func, x_range=(-2, 2), num_points=1000):
    """
    Calculates and plots both a given function and its cumulative integral over a specified range.

    Parameters:
    func (callable): The function to plot and integrate.
    x_range (tuple): A tuple of two values specifying the range (start, end) for the x-axis.
    num_points (int): The number of points to generate between the start and end of the x_range.

    Returns:
    matplotlib.axes.Axes: The Axes object containing the plots of the function and its integral.
    """
    # Generate a linearly spaced range of x-values
    x = np.linspace(x_range[0], x_range[1], num_points)
    # Calculate the function values
    y = func(x)
    # Calculate the cumulative integral using scipy's integrate module
    integral, _ = integrate.cumtrapz(y, x, initial=0)
    
    # Create a figure and an axes object
    fig, ax = plt.subplots()
    # Plot the original function
    ax.plot(x, y, label=f'{func.__name__} (x)')
    # Plot the cumulative integral
    ax.plot(x, integral, label='Cumulative Integral')
    
    # Add labels and legend
    ax.set_xlabel(f'x (range: {x_range[0]} to {x_range[1]})')
    ax.set_ylabel(f'{func.__name__}(x)')
    ax.legend()
    
    # Return the Axes object
    return ax

# Call the task_func with the sample function
ax = task_func(sample_func)
# Display the plot
plt.show()
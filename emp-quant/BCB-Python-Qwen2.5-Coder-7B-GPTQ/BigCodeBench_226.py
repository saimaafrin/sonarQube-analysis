import numpy as np
import math
import matplotlib.pyplot as plt
def task_func(range_start=0, range_end=10, step=0.1):
    """
    Generates a sequence of tuples containing x and e^x values and plots the exponential function.
    
    Parameters:
    - range_start (float): The start of the range for x values.
    - range_end (float): The end of the range for x values.
    - step (float): The step size for the range of x values.
    
    Returns:
    - generator: A generator object that yields tuples of (x, e^x).
    - Axes: The plotted Axes object of the exponential function.
    """
    # Create a generator object that yields tuples of (x, e^x)
    gen = ((x, math.exp(x)) for x in np.arange(range_start, range_end, step))
    
    # Extract x and y values from the generator
    x_values, y_values = zip(*gen)
    
    # Plot the exponential function
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values, label='e^x')
    ax.set_xlabel('x')
    ax.set_ylabel('e^x')
    ax.set_title('Exponential Function')
    ax.legend()
    
    return gen, ax
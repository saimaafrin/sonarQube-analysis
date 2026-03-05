import numpy as np
import matplotlib.pyplot as plt
import cmath
def task_func(x, y):
    """
    Draw the phase of a complex function over a range of x and y and return the matplotlib axes object along with the 2D array of calculated phase values.
    
    Parameters:
    x (numpy.ndarray): The x values.
    y (numpy.ndarray): The y values.
    
    Returns:
    tuple: containing
    matplotlib.axes.Axes: The axes object with the phase plot.
    numpy.ndarray: The 2D array of calculated phase values.
    """
    # Check if x and y are numpy arrays
    if not isinstance(x, np.ndarray) or not isinstance(y, np.ndarray):
        raise TypeError("Both x and y must be numpy.ndarray.")
    
    # Check if x and y have the same length
    if len(x) != len(y):
        raise ValueError("x and y must have the same length.")
    
    # Create a meshgrid for x and y
    X, Y = np.meshgrid(x, y)
    
    # Create a complex function
    Z = X + 1j * Y
    
    # Calculate the phase of the complex function
    phase = np.angle(Z)
    
    # Create a figure and an axes object
    fig, ax = plt.subplots()
    
    # Plot the phase
    c = ax.contourf(X, Y, phase)
    fig.colorbar(c)
    
    return ax, phase
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
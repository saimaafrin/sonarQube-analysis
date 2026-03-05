import numpy as np
import matplotlib.pyplot as plt
import cmath
def task_func(x, y):
    """
    Draw the phase of a complex function over a range of x and y and return the matplotlib axes object along with the 2D array of calculated phase values.
    The function should raise the exception for:
        TypeError: If either `x` or `y` is not a numpy.ndarray.
        ValueError: If `x` and `y` do not have the same length.
    The function should output with:
        tuple: containing
            matplotlib.axes.Axes: The axes object with the phase plot.
            numpy.ndarray: The 2D array of calculated phase values.
    """
    if not isinstance(x, np.ndarray) or not isinstance(y, np.ndarray):
        raise TypeError("x and y must be numpy.ndarray")
    if len(x) != len(y):
        raise ValueError("x and y must have the same length")

    # Calculate the phase of the complex function
    phase = np.arctan2(np.sin(x), np.cos(y))

    # Create a 2D array of phase values
    phase_array = np.zeros((len(x), len(y)))
    for i in range(len(x)):
        for j in range(len(y)):
            phase_array[i, j] = phase[i]

    # Create a matplotlib figure and axes object
    fig, ax = plt.subplots()

    # Plot the phase values as a heatmap
    ax.pcolor(phase_array, cmap="RdYlGn")

    # Set the x and y labels
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    # Return the axes object and the phase array
    return ax, phase_array
x = np.linspace(0, 2 * np.pi, 100)
y = np.linspace(0, 2 * np.pi, 100)
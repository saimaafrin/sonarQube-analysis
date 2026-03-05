
import matplotlib.pyplot as plt
import numpy as np

# Constants
FUNCTIONS = [np.sin, np.cos, np.tan]

def task_func(ax, func_index):
    """
    Draw a mathematical function (sine, cosine, or tangent) on a polar diagram 'ax'.
    The radial ticks are placed at a position corresponding to the index of the function multiplied by 45 degrees.
    """
    if not isinstance(ax, plt.Axes):
        raise ValueError("Input ax must be a matplotlib.axes._axes.Axes object.")

    # Get the function to plot
    func = FUNCTIONS[func_index]

    # Set the radial ticks
    ax.set_rmax(45 * func_index)

    # Plot the function
    ax.plot(np.linspace(0, 2 * np.pi, 100), func(np.linspace(0, 2 * np.pi, 100)))

    return ax
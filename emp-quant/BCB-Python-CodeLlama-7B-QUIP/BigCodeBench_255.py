
import matplotlib
import numpy as np
# Constants
FUNCTIONS = [np.sin, np.cos, np.tan]
def task_func(ax, func_index):
    if not isinstance(ax, matplotlib.axes.Axes):
        raise ValueError("ax must be an Axes object")
    # Set the radial ticks
    ax.set_xticks(np.arange(0, 360, 45))
    # Set the radial labels
    ax.set_xticklabels(np.arange(0, 360, 45))
    # Set the angular labels
    ax.set_yticklabels(np.arange(0, 360, 45))
    # Plot the function
    ax.plot(FUNCTIONS[func_index](np.arange(0, 360, 45)))
    return ax
import matplotlib
import numpy as np
FUNCTIONS = [np.sin, np.cos, np.tan]
def task_func(ax, func_index):
    """
    Draw a mathematical function (sine, cosine, or tangent) on a polar diagram 'ax'.
    The radial ticks are placed at a position corresponding to the index of the function multiplied by 45 degrees.
    The function should raise the exception for: This function will raise a ValueError if the input ax is not and Axes.
    The function should output with:
        matplotlib.axes._axes.Axes: The modified ax with the plotted function.
    """
    if not isinstance(ax, matplotlib.axes._axes.Axes):
        raise ValueError("Input ax must be an Axes object.")
    # Set the radial ticks
    ax.set_rgrids(np.linspace(0, 1, 4))
    # Set the angular ticks
    ax.set_tgrids(np.linspace(0, 2 * np.pi, 8))
    # Plot the function
    ax.plot(FUNCTIONS[func_index](np.linspace(0, 2 * np.pi, 100)))
    return ax
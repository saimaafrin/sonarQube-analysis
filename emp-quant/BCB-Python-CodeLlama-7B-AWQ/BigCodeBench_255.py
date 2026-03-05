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
    if not isinstance(ax, matplotlib.axes.Axes):
        raise ValueError("Input ax must be an Axes object.")
    # Set the function to plot
    func = FUNCTIONS[func_index]
    # Set the radial ticks
    ticks = np.linspace(0, 2 * np.pi, 10)
    # Plot the function
    ax.plot(ticks, func(ticks), label=f"{func.__name__} function")
    # Set the tick labels
    ax.set_xticks(ticks)
    ax.set_xticklabels(ticks * 45)
    # Set the title
    ax.set_title(f"{func.__name__} function on a polar diagram")
    return ax
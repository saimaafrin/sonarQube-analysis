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
        raise ValueError("Input ax must be a matplotlib.axes._axes.Axes object.")
    # Draw the function
    func = FUNCTIONS[func_index]
    theta = np.linspace(0, 2 * np.pi, 100)
    r = func(theta)
    ax.plot(theta, r, label=f"{func.__name__} function")
    # Set the radial ticks
    ax.set_xticks(np.linspace(0, 2 * np.pi, 5) * 45)
    ax.set_yticks(np.linspace(-1, 1, 5) * 45)
    ax.set_xticklabels(["0", "45", "90", "135", "180"])
    ax.set_yticklabels(["-1", "0", "1"])
    return ax
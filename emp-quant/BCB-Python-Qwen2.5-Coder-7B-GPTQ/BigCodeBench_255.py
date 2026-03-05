import matplotlib.pyplot as plt
import numpy as np
FUNCTIONS = [np.sin, np.cos, np.tan]
def task_func(ax, func_index):
    """
    Draws a mathematical function (sine, cosine, or tangent) on a polar diagram 'ax'.
    The radial ticks are placed at a position corresponding to the index of the function multiplied by 45 degrees.
    
    Parameters:
    ax (matplotlib.axes._axes.Axes): The axes on which to draw the function.
    func_index (int): The index of the function to draw (0 for sine, 1 for cosine, 2 for tangent).
    
    Returns:
    matplotlib.axes._axes.Axes: The modified ax with the plotted function.
    
    Raises:
    ValueError: If the input ax is not an Axes object.
    """
    if not isinstance(ax, plt.Axes):
        raise ValueError("The input ax must be a matplotlib.axes._axes.Axes object.")
    
    # Generate theta values from 0 to 2*pi
    theta = np.linspace(0, 2 * np.pi, 1000)
    
    # Calculate the function values
    r = FUNCTIONS[func_index](theta)
    
    # Plot the function on the polar axes
    ax.plot(theta, r)
    
    # Set radial ticks at 45-degree intervals
    ax.set_rticks(np.arange(0, 1.1, 0.25) * np.pi / 4)
    
    return ax
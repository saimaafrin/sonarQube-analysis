
import matplotlib
import numpy as np
# Constants
FUNCTIONS = [np.sin, np.cos, np.tan]

def task_func(ax, func_index):
    """
    Draw a mathematical function (sine, cosine, or tangent) on a polar diagram 'ax'.
    The radial ticks are placed at a position corresponding to the index of the function multiplied by 45 degrees.
    
    Args:
    ax (matplotlib.axes._subplots.AxesSubplot): The axes on which to draw the function.
    func_index (int): The index of the function to draw (0 for sine, 1 for cosine, 2 for tangent).
    
    Returns:
    matplotlib.axes._subplots.AxesSubplot: The modified ax with the plotted function.
    
    Raises:
    ValueError: If the input ax is not an instance of matplotlib.axes._subplots.AxesSubplot.
    """
    if not isinstance(ax, matplotlib.axes._subplots.AxesSubplot):
        raise ValueError("Input ax must be an instance of matplotlib.axes._subplots.AxesSubplot.")
    
    # Calculate the angle for each tick
    angles = np.arange(0, 360, 45)
    
    # Calculate the values of the function at each angle
    values = FUNCTIONS[func_index](np.radians(angles))
    
    # Plot the function on the polar diagram
    ax.plot(angles, values, 'b-')
    
    # Set the radial ticks at the specified positions
    ax.set_xticks(angles)
    
    return ax
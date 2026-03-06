
import matplotlib.pyplot as plt
import numpy as np

# Constants
FUNCTIONS = [np.sin, np.cos, np.tan]

def task_func(ax, func_index):
    """
    Draws a mathematical function (sine, cosine, or tangent) on a polar diagram 'ax'.
    
    Parameters:
    - ax: A matplotlib.axes._axes.Axes object representing the polar plot.
    - func_index: An integer indicating which function to draw (0 for sine, 1 for cosine, 2 for tangent).
    
    Returns:
    - matplotlib.axes._axes.Axes: The modified ax with the plotted function.
    
    Raises:
    - ValueError: If the input ax is not an Axes object.
    """
    if not isinstance(ax, plt.Axes):
        raise ValueError("This function will raise a ValueError if the input ax is not an Axes.")
    
    # Generate theta values from 0 to 2*pi
    theta = np.linspace(0, 2 * np.pi, 100)
    
    # Calculate the radius based on the selected function
    r = FUNCTIONS[func_index](theta)
    
    # Plot the function on the polar axis
    ax.plot(theta, r)
    
    # Set radial ticks at positions corresponding to the index of the function multiplied by 45 degrees
    ax.set_rticks([i * np.pi / 4 for i in range(8)])
    ax.set_rticklabels(['0', 'π/4', 'π/2', '3π/4', 'π', '5π/4', '3π/2', '7π/4'])
    
    return ax
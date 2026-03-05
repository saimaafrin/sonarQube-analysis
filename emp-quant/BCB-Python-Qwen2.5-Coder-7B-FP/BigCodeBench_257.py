import numpy as np
import math
import matplotlib.pyplot as plt
def task_func(ax, num_turns):
    """
    Draws a spiral on the polar diagram 'ax' with the specified number of turns 'num_turns'.
    The spiral starts at the center and expands outward with each turn. The radial ticks on the plot
    are positioned at intervals corresponding to the number of turns multiplied by 45 degrees.
    
    Parameters:
    ax (matplotlib.axes._axes.Axes): The Axes object to draw the spiral on.
    num_turns (int): The number of turns in the spiral.
    
    Returns:
    matplotlib.axes._axes.Axes: The modified Axes object with the spiral plot.
    """
    # Generate the angles for the spiral
    theta = np.linspace(0, 2 * math.pi * num_turns, 1000)
    # Generate the radii for the spiral
    r = theta
    
    # Plot the spiral
    ax.plot(theta, r, 'b-')
    
    # Set the radial ticks at intervals corresponding to the number of turns multiplied by 45 degrees
    ax.set_rticks(np.arange(0, num_turns * 45 + 1, 45))
    
    return ax
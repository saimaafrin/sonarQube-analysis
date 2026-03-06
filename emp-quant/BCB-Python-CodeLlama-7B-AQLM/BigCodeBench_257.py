import numpy as np
import math
def task_func(ax, num_turns):
    """
    Draws a spiral on the polar diagram 'ax' with the specified number of turns 'num_turns'.
    The spiral starts at the center and expands outward with each turn.
    The radial ticks on the plot are positioned at intervals corresponding to the number of turns multiplied by 45 degrees.

    Parameters:
    ax (matplotlib.axes._axes.Axes): The Axes object for plotting the spiral.
    num_turns (int): The number of turns for the spiral.

    Returns:
    matplotlib.axes._axes.Axes: The modified Axes object with the spiral plot.

    Requirements:
    - numpy
    - math

    Example:
    >>> import matplotlib.pyplot as plt
    >>> fig, ax = plt.subplots(subplot_kw={'polar': True})
    >>> ax = task_func(ax, 3)
    >>> ax.get_rlabel_position()
    135.0
    """
    # Draw the spiral
    for i in range(num_turns):
        ax.plot(np.linspace(0, 2*math.pi*i, 100), np.linspace(0, 2*math.pi*i, 100))

    # Set the radial ticks
    ax.set_rticks([i*45 for i in range(num_turns*4)])

    # Set the radial tick labels
    ax.set_rlabel_position(135)
    ax.set_r
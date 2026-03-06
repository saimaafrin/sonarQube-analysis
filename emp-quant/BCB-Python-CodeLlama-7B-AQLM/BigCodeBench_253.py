import numpy as np
import random
COLORS = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
def task_func(ax):
    """
    Generate a random sine wave function and draw it on a provided matplotlib polar subplot 'ax'. 
    The function randomly selects a color from a predefined list and sets a random position for radial labels.

    Parameters:
    ax (matplotlib.axes._axes.Axes): The ax to plot on.

    Returns:
    str: The color code (as a string) of the plotted function.

    Requirements:
    - numpy
    - random

    Example:
    >>> import matplotlib.pyplot as plt
    >>> random.seed(0)
    >>> fig = plt.figure()
    >>> ax = fig.add_subplot(111, polar=True)
    >>> color = task_func(ax)
    >>> color in COLORS
    True
    >>> plt.close()
    """
    # Generate random function
    x = np.linspace(0, 2*np.pi, 100)
    y = np.sin(x)

    # Plot function
    ax.plot(x, y)

    # Randomly select color
    color = random.choice(COLORS)

    # Randomly select radial labels
    if random.random() < 0.5:
        ax.set_rlabel_position(0)
    else:
        ax.set_rlabel_position(90)

    return color
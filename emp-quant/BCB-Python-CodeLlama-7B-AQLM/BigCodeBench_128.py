import numpy as np
import matplotlib.pyplot as plt
from random import randint
import math
def task_func(POINTS=100):
    """
    Simulates a random walk in a two-dimensional space and draws the path using matplotlib.
    The walk is determined by randomly choosing directions at each step. The function generates
    two numpy arrays representing the x and y coordinates of each step and plots these points
    to visualize the path of the walk.

    Parameters:
        POINTS (int): The number of steps in the random walk. Default is 100.

    Returns:
        A matplotlib figure object representing the plot of the random walk.

    Requirements:
        - numpy
        - matplotlib.pyplot
        - random.randint
        - math

    Examples:
        >>> import matplotlib
        >>> fig = task_func(200)  # Displays a plot of a random walk with 200 steps
        >>> isinstance(fig, matplotlib.figure.Figure)
        True
    """
    x = np.zeros(POINTS)
    y = np.zeros(POINTS)
    x[0] = 0
    y[0] = 0
    for i in range(1, POINTS):
        x[i] = x[i-1] + randint(-1, 1)
        y[i] = y[i-1] + randint(-1, 1)
    plt.plot(x, y, 'o')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Random Walk')
    return plt.gcf()
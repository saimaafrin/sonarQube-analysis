import numpy as np
import matplotlib.pyplot as plt
from random import randint
import math
def task_func(POINTS=100):
    """
    Simulates a random walk in a two-dimensional space and draws the path using matplotlib.
    The walk is determined by randomly choosing directions at each step.
    The function generates two numpy arrays representing the x and y coordinates of each step and plots these points to visualize the path of the walk.
    The function should output with:
        A matplotlib figure object representing the plot of the random walk.
    """
    # Generate random x and y coordinates for each step
    x_coords = np.random.randint(0, 100, size=POINTS)
    y_coords = np.random.randint(0, 100, size=POINTS)

    # Plot the path of the random walk
    fig, ax = plt.subplots()
    ax.plot(x_coords, y_coords, 'o-')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Random Walk')
    plt.show()

    return fig
POINTS = 100
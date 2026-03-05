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
    x = np.random.randint(0, 100, size=POINTS)
    y = np.random.randint(0, 100, size=POINTS)

    # Create a list of tuples for the x and y coordinates
    coords = list(zip(x, y))

    # Create a matplotlib figure and axis
    fig, ax = plt.subplots()

    # Plot the random walk
    ax.plot(coords, 'bo-')

    # Set the title and labels
    ax.set_title('Random Walk')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    # Return the matplotlib figure object
    return fig
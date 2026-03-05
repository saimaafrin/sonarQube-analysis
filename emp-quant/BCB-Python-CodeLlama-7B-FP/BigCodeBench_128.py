import numpy as np
import matplotlib.pyplot as plt
from random import randint
import math
def task_func(POINTS=100):
    """
    Simulates a random walk in a two-dimensional space and draws the path using matplotlib.
    The walk is determined by randomly choosing directions at each step.
    The function generates two numpy arrays representing the x and y coordinates of each step and plots these points to visualize the path of the walk.
    """
    # Generate random x and y coordinates for each step
    x = np.random.randint(0, 100, size=POINTS)
    y = np.random.randint(0, 100, size=POINTS)

    # Plot the path of the walk
    plt.plot(x, y, 'bo-')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Random Walk')
    plt.show()
POINTS = 100

import numpy as np
import matplotlib.pyplot as plt
from random import randint
import math

def task_func(POINTS=100):
    # Initialize the x and y coordinates of the walk
    x = np.zeros(POINTS)
    y = np.zeros(POINTS)

    # Set the starting point of the walk
    x[0] = 0
    y[0] = 0

    # Simulate the random walk
    for i in range(1, POINTS):
        # Choose a random direction
        direction = randint(0, 3)

        # Update the coordinates based on the direction
        if direction == 0:
            x[i] = x[i-1] + 1
            y[i] = y[i-1]
        elif direction == 1:
            x[i] = x[i-1] - 1
            y[i] = y[i-1]
        elif direction == 2:
            x[i] = x[i-1]
            y[i] = y[i-1] + 1
        else:
            x[i] = x[i-1]
            y[i] = y[i-1] - 1

    # Plot the walk
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Random Walk')
    plt.show()

# Call the function
task_func(POINTS=100)
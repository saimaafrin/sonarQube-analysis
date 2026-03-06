
import numpy as np
import matplotlib.pyplot as plt
from random import randint
import math

def task_func(POINTS=100):
    # Initialize arrays to store x and y coordinates
    x_coords = np.zeros(POINTS)
    y_coords = np.zeros(POINTS)

    # Set the starting point
    x_coords[0] = 0
    y_coords[0] = 0

    # Perform the random walk
    for i in range(1, POINTS):
        # Choose a random direction
        direction = randint(0, 3)

        # Update the coordinates based on the direction
        if direction == 0:
            x_coords[i] = x_coords[i-1] + 1
            y_coords[i] = y_coords[i-1]
        elif direction == 1:
            x_coords[i] = x_coords[i-1] - 1
            y_coords[i] = y_coords[i-1]
        elif direction == 2:
            x_coords[i] = x_coords[i-1]
            y_coords[i] = y_coords[i-1] + 1
        else:
            x_coords[i] = x_coords[i-1]
            y_coords[i] = y_coords[i-1] - 1

    # Plot the path
    fig, ax = plt.subplots()
    ax.plot(x_coords, y_coords, 'bo-')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Random Walk')
    plt.show()

# Call the function
task_func(POINTS=100)
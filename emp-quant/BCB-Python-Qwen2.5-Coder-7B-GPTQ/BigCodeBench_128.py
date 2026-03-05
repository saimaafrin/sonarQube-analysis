import numpy as np
import matplotlib.pyplot as plt
from random import randint
import math
def task_func(POINTS=100):
    # Initialize the arrays to store the x and y coordinates
    x = np.zeros(POINTS)
    y = np.zeros(POINTS)
    
    # Directions: 0=up, 1=down, 2=left, 3=right
    directions = [0, 1, 2, 3]
    
    # Starting point
    x[0], y[0] = 0, 0
    
    # Generate random walk
    for i in range(1, POINTS):
        direction = directions[randint(0, 3)]
        if direction == 0:  # up
            y[i] = y[i-1] + 1
            x[i] = x[i-1]
        elif direction == 1:  # down
            y[i] = y[i-1] - 1
            x[i] = x[i-1]
        elif direction == 2:  # left
            x[i] = x[i-1] - 1
            y[i] = y[i-1]
        elif direction == 3:  # right
            x[i] = x[i-1] + 1
            y[i] = y[i-1]
    
    # Plot the random walk
    plt.figure(figsize=(10, 10))
    plt.plot(x, y, marker='o', linestyle='-', color='b')
    plt.title('2D Random Walk')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.grid(True)
    plt.show()
    
    # Return the figure object
    return plt.gcf()
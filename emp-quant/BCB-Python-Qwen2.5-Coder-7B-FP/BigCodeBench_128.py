import numpy as np
import matplotlib.pyplot as plt
from random import randint
import math
def task_func(POINTS=100):
    # Initialize the starting point
    x = np.zeros(POINTS)
    y = np.zeros(POINTS)
    
    # Directions: 0=up, 1=right, 2=down, 3=left
    directions = [0, 1, 2, 3]
    
    # Generate random walk
    for i in range(1, POINTS):
        direction = directions[randint(0, 3)]
        if direction == 0:
            y[i] = y[i-1] + 1
        elif direction == 1:
            x[i] = x[i-1] + 1
        elif direction == 2:
            y[i] = y[i-1] - 1
        elif direction == 3:
            x[i] = x[i-1] - 1
    
    # Plot the random walk
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, marker='o', linestyle='-', color='b')
    plt.title('Random Walk in 2D Space')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.grid(True)
    plt.show()
    
    return plt

import numpy as np
import matplotlib.pyplot as plt
from random import randint
import math

def task_func(POINTS=100):
    # Initialize the starting point
    x = np.zeros(POINTS)
    y = np.zeros(POINTS)
    
    # Directions: 0=North, 1=East, 2=South, 3=West
    directions = [0, 1, 2, 3]
    
    # Simulate the random walk
    for i in range(1, POINTS):
        # Randomly choose a direction
        direction = directions[randint(0, 3)]
        
        # Update the position based on the direction
        if direction == 0:
            y[i] = y[i-1] + 1
        elif direction == 1:
            x[i] = x[i-1] + 1
        elif direction == 2:
            y[i] = y[i-1] - 1
        elif direction == 3:
            x[i] = x[i-1] - 1
    
    # Create the plot
    fig, ax = plt.subplots()
    ax.plot(x, y, marker='o')
    ax.set_title('Random Walk in 2D')
    ax.set_xlabel('X Coordinate')
    ax.set_ylabel('Y Coordinate')
    ax.grid(True)
    
    return fig
import numpy as np
import matplotlib.pyplot as plt
from random import randint
import math
def task_func(POINTS=100):
    # Initialize the arrays to store the x and y coordinates
    x_coords = np.zeros(POINTS)
    y_coords = np.zeros(POINTS)
    
    # Starting point
    x_coords[0], y_coords[0] = 0, 0
    
    # Directions: 0 - left, 1 - up, 2 - right, 3 - down
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    
    # Generate the random walk
    for i in range(1, POINTS):
        # Randomly choose a direction
        dx, dy = directions[randint(0, 3)]
        # Update the coordinates
        x_coords[i] = x_coords[i-1] + dx
        y_coords[i] = y_coords[i-1] + dy
    
    # Create a figure and axis
    fig, ax = plt.subplots()
    # Plot the random walk
    ax.plot(x_coords, y_coords, marker='o')
    # Set the title and labels
    ax.set_title('Random Walk in 2D Space')
    ax.set_xlabel('X Coordinate')
    ax.set_ylabel('Y Coordinate')
    
    # Return the figure object
    return fig

import numpy as np
import matplotlib.pyplot as plt
from random import randint
import math

def task_func(POINTS=100):
    # Initialize the starting point
    x = [0]
    y = [0]

    # Directions: 0 - left, 1 - right, 2 - up, 3 - down
    for _ in range(1, POINTS):
        direction = randint(0, 3)
        if direction == 0:
            x.append(x[-1] - 1)
            y.append(y[-1])
        elif direction == 1:
            x.append(x[-1] + 1)
            y.append(y[-1])
        elif direction == 2:
            x.append(x[-1])
            y.append(y[-1] + 1)
        else:
            x.append(x[-1])
            y.append(y[-1] - 1)

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Plot the random walk
    ax.plot(x, y, marker='o')

    # Set the title and labels
    ax.set_title('Random Walk')
    ax.set_xlabel('X Coordinate')
    ax.set_ylabel('Y Coordinate')

    return fig
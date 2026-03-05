
import numpy as np
import matplotlib.pyplot as plt
from random import randint
import math

def task_func(POINTS=100):
    # Initialize the x and y coordinates of the first point
    x = 0
    y = 0

    # Create a list to store the x and y coordinates of each step
    points = []

    # Define the function to randomly choose the direction of the walk
    def random_direction():
        return randint(0, 3)

    # Define the function to move in a random direction
    def move(direction):
        if direction == 0:
            x += 1
        elif direction == 1:
            y += 1
        elif direction == 2:
            x -= 1
        elif direction == 3:
            y -= 1

    # Define the function to generate the random walk
    def generate_walk(POINTS):
        for i in range(POINTS):
            direction = random_direction()
            move(direction)
            points.append([x, y])

    # Generate the random walk
    generate_walk(POINTS)

    # Plot the points
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(points[:, 0], points[:, 1])
    plt.show()

    return fig
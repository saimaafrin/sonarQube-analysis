import numpy as np
import random
import matplotlib.pyplot as plt
COLORS = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
def task_func(ax):
    # Generate a random sine wave function
    x = np.linspace(0, 2 * np.pi, 1000)
    y = np.sin(x)

    # Randomly select a color from the predefined list
    color = random.choice(COLORS)

    # Set a random position for radial labels
    label_position = random.randint(0, 100)

    # Plot the sine wave function
    ax.plot(x, y, color=color)

    # Add radial labels
    ax.set_rlabel_position(label_position)

    # Return the color code of the plotted function
    return color
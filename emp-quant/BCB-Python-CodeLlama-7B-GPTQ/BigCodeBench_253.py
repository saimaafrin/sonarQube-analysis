import numpy as np
import random
import matplotlib.pyplot as plt
COLORS = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
def task_func(ax):
    # Generate a random sine wave function
    t = np.linspace(0, 2 * np.pi, 1000)
    y = np.sin(t)

    # Randomly select a color from the predefined list
    color = random.choice(COLORS)

    # Set a random position for radial labels
    labels = np.linspace(0, 1, 10)
    labels = np.random.permutation(labels)

    # Plot the sine wave function
    ax.plot(t, y, color=color)

    # Add radial labels
    for label in labels:
        ax.text(0, label, f'{label:.2f}', ha='center', va='center')

    # Return the color code of the plotted function
    return color
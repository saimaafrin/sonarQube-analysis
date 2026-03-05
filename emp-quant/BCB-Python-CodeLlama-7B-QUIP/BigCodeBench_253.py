
import numpy as np
import random
# Constants
COLORS = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
def task_func(ax):
    # Generate a random sine wave
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)
    # Select a random color from the list
    color = random.choice(COLORS)
    # Set a random position for radial labels
    label_pos = random.randint(1, 10)
    # Plot the sine wave
    ax.plot(x, y, color=color)
    # Add radial labels
    ax.set_rlabel_position(label_pos)
    return color
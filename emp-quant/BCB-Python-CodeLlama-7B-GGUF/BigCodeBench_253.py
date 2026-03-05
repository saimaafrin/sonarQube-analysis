
import numpy as np
import random
import matplotlib.pyplot as plt

# Constants
COLORS = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

def task_func(ax):
    # Generate random sine wave function
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)

    # Select random color from predefined list
    color = random.choice(COLORS)

    # Set random position for radial labels
    labels = np.linspace(0, 1, 10)
    labels = labels[np.random.choice(len(labels), 5, replace=False)]

    # Plot sine wave function
    ax.plot(x, y, color=color)

    # Add radial labels
    for label in labels:
        ax.text(label, 1.1, f'{label:.1f}', ha='center', va='bottom')

    # Return color code
    return color

# Create polar subplot
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

# Call task function and get color code
color = task_func(ax)

# Set title and show plot
ax.set_title(f'Random sine wave function with color {color}')
plt.show()
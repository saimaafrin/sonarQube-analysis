import numpy as np
import random
import matplotlib.pyplot as plt
COLORS = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
def task_func(ax):
    # Generate random data for the sine wave
    theta = np.linspace(0, 2 * np.pi, 100)
    r = np.sin(theta) + np.random.normal(0, 0.1, 100)
    
    # Randomly select a color
    color = random.choice(COLORS)
    
    # Plot the sine wave on the provided polar subplot
    ax.plot(theta, r, color=color)
    
    # Set a random position for radial labels
    ax.set_rticks([0.5, 1, 1.5, 2])  # Set the radial ticks
    ax.set_rlabel_position(random.randint(0, 360))  # Set a random position for the radial labels
    
    # Return the color code of the plotted function
    return color
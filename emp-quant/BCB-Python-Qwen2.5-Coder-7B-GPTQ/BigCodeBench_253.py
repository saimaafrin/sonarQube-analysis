import numpy as np
import random
import matplotlib.pyplot as plt
COLORS = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
def task_func(ax):
    # Generate random parameters for the sine wave
    amplitude = random.uniform(0.5, 1.5)
    frequency = random.uniform(0.1, 0.5)
    phase = random.uniform(0, 2 * np.pi)
    
    # Generate the x values (angles in radians)
    x = np.linspace(0, 2 * np.pi, 100)
    
    # Calculate the y values (sine wave)
    y = amplitude * np.sin(frequency * x + phase)
    
    # Select a random color from the predefined list
    color = random.choice(COLORS)
    
    # Plot the sine wave on the provided polar subplot
    ax.plot(x, y, color=color)
    
    # Set a random position for radial labels
    ax.set_rticks(np.arange(0, 2 * np.pi, np.pi / 4))
    ax.set_rlabel_position(random.uniform(0, 360))
    
    # Return the color code of the plotted function
    return color
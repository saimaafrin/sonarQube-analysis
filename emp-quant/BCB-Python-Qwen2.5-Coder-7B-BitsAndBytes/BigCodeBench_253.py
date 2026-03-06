
import numpy as np
import random
from matplotlib.ticker import MaxNLocator

# Constants
COLORS = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

def task_func(ax):
    # Generate random parameters for the sine wave
    amplitude = random.uniform(0.5, 2.0)
    frequency = random.uniform(0.1, 2.0)
    phase = random.uniform(0, 2 * np.pi)
    
    # Generate x values
    t = np.linspace(0, 2 * np.pi, 100)
    
    # Calculate y values for the sine wave
    y = amplitude * np.sin(frequency * t + phase)
    
    # Randomly select a color from the COLORS list
    color = random.choice(COLORS)
    
    # Plot the sine wave
    ax.plot(t, y, color=color)
    
    # Set a random position for radial labels
    ax.set_rticks([np.random.uniform(0.2, 1.8), np.random.uniform(0.4, 1.6), np.random.uniform(0.6, 1.4)])
    ax.set_rlabel_position(np.random.randint(0, 360))
    
    # Return the color code
    return color

import numpy as np
import random
import matplotlib.pyplot as plt

# Constants
COLORS = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

def task_func(ax):
    # Generate random data for the sine wave
    theta = np.linspace(0, 2 * np.pi, 100)
    amplitude = random.uniform(0.5, 1.5)
    phase = random.uniform(0, 2 * np.pi)
    sine_wave = amplitude * np.sin(theta + phase)
    
    # Randomly select a color from the predefined list
    color = random.choice(COLORS)
    
    # Plot the sine wave
    ax.plot(theta, sine_wave, color=color)
    
    # Set a random position for radial labels
    ax.set_theta_offset(random.uniform(0, 2 * np.pi))
    
    # Return the color code of the plotted function
    return color
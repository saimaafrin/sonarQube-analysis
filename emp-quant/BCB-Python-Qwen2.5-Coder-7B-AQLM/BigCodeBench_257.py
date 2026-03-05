
import numpy as np
import math
import matplotlib.pyplot as plt

def task_func(ax, num_turns):
    # Generate the spiral data
    theta = np.linspace(0, 2 * math.pi * num_turns, 1000)
    r = theta / (2 * math.pi)
    
    # Plot the spiral
    ax.plot(r, theta)
    
    # Set the radial ticks at intervals corresponding to the number of turns multiplied by 45 degrees
    ax.set_yticks(np.arange(0, 2 * math.pi * num_turns + 0.1, math.pi / 4))
    ax.set_yticklabels([f'{int(t / (math.pi / 4)) * 45}°' for t in ax.get_yticks()])
    
    # Return the modified Axes object
    return ax
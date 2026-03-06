
import numpy as np
import math
import matplotlib.pyplot as plt

def task_func(ax, num_turns):
    # Generate theta values for the spiral
    theta = np.linspace(0, num_turns * 2 * math.pi, 1000)
    
    # Calculate radius values for the spiral
    r = theta
    
    # Plot the spiral
    ax.plot(r * np.cos(theta), r * np.sin(theta))
    
    # Set the aspect ratio to be equal so that the spiral looks circular
    ax.set_aspect('equal')
    
    # Set the radial ticks at intervals corresponding to the number of turns multiplied by 45 degrees
    ax.set_yticks(np.arange(0, num_turns * 2 + 1) * (math.pi / 4))
    
    return ax
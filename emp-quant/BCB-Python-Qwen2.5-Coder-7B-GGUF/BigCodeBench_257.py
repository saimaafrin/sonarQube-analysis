
import numpy as np
import math
import matplotlib.pyplot as plt

def task_func(ax, num_turns):
    # Generate theta values for the spiral
    theta = np.linspace(0, num_turns * 2 * math.pi, 1000)
    # Calculate the radius for each theta value
    r = theta
    
    # Plot the spiral
    ax.plot(r, theta, color='blue')
    
    # Set the radial ticks at intervals corresponding to the number of turns multiplied by 45 degrees
    ax.set_rticks(np.arange(0, num_turns * 2 * math.pi, math.pi / 4))
    
    # Set the theta tick labels to be empty
    ax.set_xticklabels([])
    
    return ax
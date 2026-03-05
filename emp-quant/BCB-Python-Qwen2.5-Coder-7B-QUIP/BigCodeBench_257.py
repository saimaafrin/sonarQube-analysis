
import numpy as np
import math
def task_func(ax, num_turns):
    # Generate angles for the spiral
    angles = np.linspace(0, num_turns * 2 * math.pi, 1000)
    # Calculate the radius for each angle
    radius = np.linspace(0, 10, 1000)
    # Convert angles to radians
    angles = np.deg2rad(angles)
    # Calculate x and y coordinates
    x = radius * np.cos(angles)
    y = radius * np.sin(angles)
    # Plot the spiral
    ax.plot(x, y)
    # Set the number of ticks on the radial axis
    ax.set_xticks(np.arange(0, num_turns * 45 + 1, 45))
    # Return the modified Axes object
    return ax
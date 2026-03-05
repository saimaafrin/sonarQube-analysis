
import matplotlib.pyplot as plt
import numpy as np

# Constants
FUNCTIONS = [np.sin, np.cos, np.tan]

def task_func(ax, func_index):
    if not isinstance(ax, plt.Axes):
        raise ValueError("The input ax must be a matplotlib.axes._axes.Axes object.")
    
    # Generate theta values from 0 to 2*pi
    theta = np.linspace(0, 2 * np.pi, 100)
    
    # Calculate the function values
    r = FUNCTIONS[func_index](theta)
    
    # Plot the function on the polar axes
    ax.plot(theta, r)
    
    # Set radial ticks at 45-degree intervals
    ax.set_yticks(np.arange(0, 1.1, 0.25) * np.pi / 4)
    ax.set_yticklabels([f"{int(t * 45)}°" for t in np.arange(0, 1.1, 0.25)])
    
    return ax
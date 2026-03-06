
import matplotlib.pyplot as plt
import numpy as np

def task_func(ax, radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    
    if ax.projection != 'polar':
        raise TypeError("The provided axis must be a polar plot.")
    
    # Generate points for the circle
    theta = np.linspace(0, 2 * np.pi, 100)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    
    # Plot the circle
    ax.plot(x, y)
    
    # Set radial ticks
    ax.set_rticks(np.arange(0, radius + 1, 1))
    
    return ax
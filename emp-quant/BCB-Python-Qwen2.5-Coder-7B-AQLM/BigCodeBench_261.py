
import matplotlib.pyplot as plt
import numpy as np

def task_func(ax, radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    if not ax.get_typekit().get_name().startswith('polar'):
        raise TypeError("The provided axis is not a polar plot")
    
    # Draw a circle with the given radius
    theta = np.linspace(0, 2 * np.pi, 100)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    ax.plot(x, y)
    
    # Set radial ticks
    ax.set_yticks(np.arange(0, radius + 1, 1))
    
    return ax
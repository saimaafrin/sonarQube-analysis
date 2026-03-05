
import matplotlib.pyplot as plt
import numpy as np

def task_func(ax, radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    if not ax.name == 'polar':
        raise TypeError("The provided axis is not a polar plot")
    
    theta = np.linspace(0, 2 * np.pi, 100)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    
    ax.plot(x, y)
    ax.set_rticks(np.arange(0, radius + 1, 1))
    
    return ax
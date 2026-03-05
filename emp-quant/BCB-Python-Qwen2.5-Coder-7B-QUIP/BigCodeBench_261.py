
import matplotlib.pyplot as plt
import numpy as np

def task_func(ax, radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    if not ax.get_projection() == 'polar':
        raise TypeError("The provided axes is not a polar plot")
    
    theta = np.linspace(0, 2 * np.pi, 100)
    r = radius
    ax.plot(theta, r, 'b-')  # 'b-' for blue line
    ax.set_rticks([radius])  # Set radial ticks
    ax.set_rorigin(0)  # Set the origin of the radial axis
    ax.set_title(f"Circle with radius {radius}")
    return ax
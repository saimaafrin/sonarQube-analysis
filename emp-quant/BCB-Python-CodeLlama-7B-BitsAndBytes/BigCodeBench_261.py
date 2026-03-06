
import matplotlib.pyplot as plt
import numpy as np

def task_func(ax, radius):
    if not isinstance(ax, plt.PolarAxes):
        raise TypeError("ax must be a polar plot")
    if radius < 0:
        raise ValueError("radius must be non-negative")

    # Create a circle in the polar plot
    theta = np.linspace(0, 2 * np.pi, 100)
    r = radius
    ax.plot(r * np.cos(theta), r * np.sin(theta), color='blue')

    # Set radial ticks
    ax.set_rgrids([0.5, 1, 1.5, 2])

    return ax
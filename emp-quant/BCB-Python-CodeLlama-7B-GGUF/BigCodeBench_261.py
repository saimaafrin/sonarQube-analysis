
import matplotlib.pyplot as plt
import numpy as np

def task_func(ax, radius):
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    if not isinstance(ax, plt.PolarAxes):
        raise TypeError("ax must be a polar plot")

    # Draw the circle
    theta = np.linspace(0, 2 * np.pi, 100)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    ax.plot(x, y, color="red")

    # Set radial ticks
    ax.set_rmax(radius)
    ax.set_rticks([0.5, 1, 2, 5])
    ax.set_rlabel_position(-22.5)

    return ax
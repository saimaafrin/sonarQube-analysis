
import matplotlib.pyplot as plt
import numpy as np

def task_func(ax, radius):
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    if not isinstance(ax, plt.PolarAxes):
        raise TypeError("ax must be a PolarAxes object")
    ax.set_xlim(0, radius)
    ax.set_ylim(0, radius)
    ax.set_xlabel("Distance from the center")
    ax.set_ylabel("Distance from the center")
    ax.set_title("Circle")
    ax.grid(True)
    ax.set_aspect("equal")
    ax.set_xticks(np.arange(0, radius, 0.1))
    ax.set_yticks(np.arange(0, radius, 0.1))
    ax.set_xticklabels(np.arange(0, radius, 0.1))
    ax.set_yticklabels(np.arange(0, radius, 0.1))
    ax.grid(True)
    return ax
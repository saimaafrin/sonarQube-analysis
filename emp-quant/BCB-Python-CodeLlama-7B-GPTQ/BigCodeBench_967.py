import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
def task_func(func, x_range=(-2, 2), num_points=1000):
    """
    Calculates and plots both a given function and its cumulative integral over a specified range, using a linearly spaced range of x-values.
    """
    x = np.linspace(x_range[0], x_range[1], num_points)
    y = func(x)
    y_cum = integrate.cumulative_trapezoid(y, x)
    fig, ax = plt.subplots()
    ax.plot(x, y, label=f"{func.__name__}")
    ax.plot(x, y_cum, label=f"{func.__name__} integral")
    ax.legend()
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    return ax
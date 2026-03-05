
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def task_func(func, x_range=(-2, 2), num_points=1000):
    x = np.linspace(x_range[0], x_range[1], num_points)
    y = func(x)
    integral = integrate.cumulative_trapezoid(y, x)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title(f"{func.__name__} Integral")
    ax.legend()
    return ax

def plot_func(func, x_range=(-2, 2), num_points=1000):
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title(f"{func.__name__} Function")
    ax.legend()
    return ax

def main():
    func = lambda x: x**2
    x_range = (-2, 2)
    num_points = 1000
    fig, ax = plot_func(func, x_range, num_points)
    ax = task_func(func, x_range, num_points)
    fig.show()
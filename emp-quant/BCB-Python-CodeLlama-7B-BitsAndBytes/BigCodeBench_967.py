
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def task_func(func, x_range=(-2, 2), num_points=1000):
    # Define the function to integrate
    def f(x):
        return x**2

    # Define the range of x-values
    x = np.linspace(x_range[0], x_range[1], num_points)

    # Calculate the integral of the function
    integral = integrate.quad(f, x_range[0], x_range[1])

    # Plot the function and its integral
    fig, ax = plt.subplots()
    ax.plot(x, f(x), label='Function')
    ax.plot(x, integral, label='Integral')
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.legend()
    return ax
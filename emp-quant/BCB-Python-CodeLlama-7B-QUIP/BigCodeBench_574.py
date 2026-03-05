
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np

def task_func(array_length=100, noise_level=0.2):
    # Generate a noisy sine wave
    x = np.linspace(0, 2 * np.pi, array_length)
    y = np.sin(x)
    y += np.random.normal(0, noise_level, array_length)

    # Define the curve to adjust
    def func(x, a, b):
        return a * np.sin(x) + b

    # Perform curve_fit
    popt, _ = curve_fit(func, x, y)

    # Plot the results
    plt.plot(x, y, label='Noisy sine wave')
    plt.plot(x, func(x, *popt), label='Adjusted curve')
    plt.legend()
    plt.show()

    return plt

task_func(array_length=100, noise_level=0.2)
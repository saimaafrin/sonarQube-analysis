
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np

def task_func(array_length=100, noise_level=0.2):
    # Generate a noisy sine wave
    x = np.linspace(0, 2 * np.pi, array_length)
    y = np.sin(x) + noise_level * np.random.randn(array_length)

    # Define the curve fitting function
    def sine_func(x, a, b, c, d):
        return a * np.sin(b * x + c) + d

    # Perform curve fitting
    popt, _ = curve_fit(sine_func, x, y)

    # Plot the original and adjusted curves
    fig, ax = plt.subplots()
    ax.plot(x, y, 'o', label='Noisy data')
    ax.plot(x, sine_func(x, *popt), 'r-', label='Adjusted curve')
    ax.legend()
    plt.show()

    return ax
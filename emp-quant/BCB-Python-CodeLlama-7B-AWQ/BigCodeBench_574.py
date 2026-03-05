from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np
def task_func(array_length=100, noise_level=0.2):
    # Generate a noisy sine wave
    x = np.linspace(0, 2 * np.pi, array_length)
    y = np.sin(x) + np.random.normal(0, noise_level, array_length)

    # Define the function to fit the data
    def func(x, a, b):
        return a * np.sin(b * x)

    # Perform the curve fit
    popt, _ = curve_fit(func, x, y)

    # Plot the data and the adjusted curve
    plt.plot(x, y, 'bo', label='Noisy data')
    plt.plot(x, func(x, *popt), 'r', label='Adjusted curve')
    plt.legend()
    plt.show()
array_length = 100
noise_level = 0.2

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def task_func(x, y, labels):
    # Define the exponential curve function
    def exp_curve(x, a, b, c):
        return a * np.exp(-b * x) + c

    # Fit the curve to the data
    popt, _ = curve_fit(exp_curve, x, y)

    # Plot the fitted curve
    plt.plot(x, y, 'bo', label='Data')
    plt.plot(x, exp_curve(x, *popt), 'r-', label='Fitted Curve')
    plt.legend()
    plt.show()

# Generate some random data
x = np.linspace(0, 10, 100)
y = np.random.normal(0, 1, 100)

# Fit the curve to the data
task_func(x, y, 'Random Data')

# Fit the curve to the data with a different label
x = np.linspace(0, 10, 100)
y = np.random.normal(0, 1, 100)
task_func(x, y, 'Another Random Data')
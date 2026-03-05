
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np

def task_func(l, x_data, plot=False):
    # Define the quadratic function
    def quadratic(x, a, b, c):
        return a * x**2 + b * x + c

    # Perform the curve fitting
    params, _ = curve_fit(quadratic, x_data, l)

    # Generate fitted values
    fitted_values = quadratic(x_data, *params)

    # Plot the original data and the fitted curve if plot=True
    if plot:
        fig, ax = plt.subplots()
        ax.scatter(x_data, l, label='Original data')
        ax.plot(x_data, fitted_values, label='Fitted curve', color='r')
        ax.legend()
        plt.show()

    # Return the parameters and fitted values
    return params, fitted_values, ax if plot else None
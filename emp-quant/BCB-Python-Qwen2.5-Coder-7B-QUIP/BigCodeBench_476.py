
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def task_func(X, Y):
    # Define the quadratic function
    def quadratic_func(x, a, b, c):
        return a * x**2 + b * x + c

    # Use curve_fit to fit the quadratic function to the data
    popt, _ = curve_fit(quadratic_func, X, Y)

    # Plot the data and the fit
    fig, ax = plt.subplots()
    ax.scatter(X, Y, label='Data')
    ax.plot(X, quadratic_func(X, *popt), 'r-', label='Fit')

    # Add labels and legend
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.legend()

    return popt, ax
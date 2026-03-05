import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
def task_func(x, y, labels):
    """
    Fit an exponential curve to given data points and plot the curves with labels.
    """
    # Define the function to be fit
    def func(x, a, b, c):
        return a * np.exp(-b * x) + c

    # Initialize the parameters
    popt, _ = curve_fit(func, x, y)

    # Plot the data and the fitted curve
    plt.plot(x, y, 'bo', label='Data')
    plt.plot(x, func(x, *popt), 'r-', label='Fitted Curve')
    plt.legend()

    # Set the labels
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Exponential Curve Fit')

    return plt.gcf()
x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 2, 3, 4, 5])
labels = ['Data', 'Fitted Curve']
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
def task_func(x, y, labels):
    """
    Fit an exponential curve to given data points and plot the curves with labels.
    """
    # Define the exponential curve function
    def exp_func(x, a, b, c):
        return a * np.exp(-b * x) + c

    # Fit the exponential curve to the data points
    popt, _ = curve_fit(exp_func, x, y)

    # Plot the fitted curve
    plt.plot(x, y, 'bo', label='Original Data')
    plt.plot(x, exp_func(x, *popt), 'r-', label='Fitted Curve')
    plt.legend()
    plt.show()

    return plt.gcf()
x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 2, 3, 4, 5])
labels = ['Data 1', 'Data 2']
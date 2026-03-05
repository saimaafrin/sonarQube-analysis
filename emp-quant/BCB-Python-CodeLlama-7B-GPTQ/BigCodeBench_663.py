import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
def task_func(x, y, labels):
    """
    Fit an exponential curve to given data points and plot the curves with labels.
    """
    # Define the function to be fitted
    def exponential_func(x, a, b, c):
        return a * np.exp(-b * x) + c

    # Fit the function to the data
    popt, _ = curve_fit(exponential_func, x, y)

    # Plot the fitted curve
    plt.plot(x, y, 'bo', label='Data')
    plt.plot(x, exponential_func(x, *popt), 'r-', label='Fitted curve')
    plt.legend()
    plt.show()
x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 2, 3, 4, 5])
labels = ['Data', 'Fitted curve']
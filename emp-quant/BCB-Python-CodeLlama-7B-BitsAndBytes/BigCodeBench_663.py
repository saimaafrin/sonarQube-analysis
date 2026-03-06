
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def task_func(x, y, labels):
    # Define the exponential curve
    def exp_curve(x, a, b, c):
        return a * np.exp(-b * x) + c

    # Fit the curve to the data
    popt, _ = curve_fit(exp_curve, x, y)

    # Plot the data and the fitted curve
    plt.plot(x, y, 'bo', label='Data')
    plt.plot(x, exp_curve(x, *popt), 'r-', label='Fitted Curve')
    plt.legend()

    # Return the figure object
    return plt.gcf()

x2 = np.array([1, 2, 3, 4, 5])
y2 = np.array([2, 4, 6, 8, 10])
labels2 = ['Data 2']

fig = task_func(x1, y1, labels1)
fig.show()

fig = task_func(x2, y2, labels2)
fig.show()
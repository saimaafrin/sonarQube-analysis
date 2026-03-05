import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
def task_func(X, Y):
    # Define the quadratic function
    def quadratic(x, a, b, c):
        return a * x ** 2 + b * x + c

    # Fit the data to the quadratic function
    popt, _ = curve_fit(quadratic, X, Y)

    # Plot the data and the fit
    plt.scatter(X, Y)
    plt.plot(X, quadratic(X, *popt), 'r-')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Quadratic Fit')
    plt.show()

    # Return the optimized parameters
    return popt
X = np.array([1, 2, 3, 4, 5])
Y = np.array([1, 4, 9, 16, 25])
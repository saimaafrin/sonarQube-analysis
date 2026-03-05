
import matplotlib.pyplot as plt
import scipy.optimize as optimize
import numpy as np

def task_func(array, target_value):
    # Define the function to fit
    def func(x, a, b):
        return a * np.exp(-b * x)

    # Define the initial guess for the parameters
    a0 = 1
    b0 = 1

    # Perform the fit
    result = optimize.curve_fit(func, array, target_value, p0=[a0, b0])

    # Extract the optimized parameters
    popt = result.x

    # Plot the data and the fit
    plt.plot(array, func(array, *popt), label='Fit')
    plt.plot(array, target_value, label='Target')
    plt.legend()
    plt.show()

    return popt, plt.gca()
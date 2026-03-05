import matplotlib.pyplot as plt
import scipy.optimize as optimize
import numpy as np
def task_func(array, target_value):
    # Define the function to be fitted
    def exponential_decay(x, a, b, c):
        return a * np.exp(-b * x) + c

    # Find the indices in the array where the first column matches the target value
    indices = np.where(array[:, 0] == target_value)[0]

    # Fit the function to the indices
    popt, _ = optimize.curve_fit(exponential_decay, array[indices, 1], array[indices, 2])

    # Plot the data and the fitted function
    fig, ax = plt.subplots()
    ax.plot(array[:, 1], array[:, 2], 'bo', label='Data')
    ax.plot(array[:, 1], exponential_decay(array[:, 1], *popt), 'r', label='Fitted function')
    ax.legend()
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Exponential Decay Fitting')

    return popt, ax
array = np.array([
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3],
    [4, 4, 4],
    [5, 5, 5],
    [6, 6, 6],
    [7, 7, 7],
    [8, 8, 8],
    [9, 9, 9],
    [10, 10, 10],
])
import matplotlib.pyplot as plt
import scipy.optimize as optimize
import numpy as np
def task_func(array, target_value):
    """
    Fit an exponential decay function to the indices in the array where the first column matches the target value.
    """
    # Find the indices of the target value in the first column
    target_indices = np.where(array[:, 0] == target_value)[0]

    # Extract the indices from the array
    x = array[target_indices, 1]
    y = array[target_indices, 2]

    # Define the exponential decay function
    def func(x, a, b, c):
        return a * np.exp(-b * x) + c

    # Initialize the parameters
    a = 1
    b = 1
    c = 0

    # Perform the optimization
    popt, _ = optimize.curve_fit(func, x, y, p0=[a, b, c])

    # Plot the data and the fit
    fig, ax = plt.subplots()
    ax.plot(x, y, 'bo', label='Data')
    ax.plot(x, func(x, *popt), 'r', label='Fit')
    ax.legend()
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Exponential Decay Fit')

    return popt, ax
array = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5]])
target_value = 3
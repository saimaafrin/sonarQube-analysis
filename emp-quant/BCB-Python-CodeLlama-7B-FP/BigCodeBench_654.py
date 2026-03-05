import matplotlib.pyplot as plt
import scipy.optimize as optimize
import numpy as np
def task_func(array, target_value):
    """
    Fit an exponential decay function to the indices in the array where the first column matches the target value.
    """
    # Find the indices of the target value in the first column
    target_indices = np.where(array[:, 0] == target_value)[0]

    # Extract the corresponding values from the second column
    target_values = array[target_indices, 1]

    # Define the exponential decay function
    def exp_decay(x, a, b, c):
        return a * np.exp(-b * x) + c

    # Perform the non-linear least squares fit
    popt, _ = optimize.curve_fit(exp_decay, target_values, target_indices)

    # Plot the data and the fitted function
    fig, ax = plt.subplots()
    ax.plot(target_values, target_indices, 'bo', label='Data')
    ax.plot(target_values, exp_decay(target_values, *popt), 'r', label='Fitted function')
    ax.legend()
    ax.set_xlabel('Value')
    ax.set_ylabel('Index')
    ax.set_title('Exponential Decay Fit')

    return popt, ax
array = np.array([[1, 2], [2, 4], [3, 6], [4, 8], [5, 10]])
target_value = 3
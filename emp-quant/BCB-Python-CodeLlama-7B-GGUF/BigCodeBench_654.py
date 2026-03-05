
import matplotlib.pyplot as plt
import scipy.optimize as optimize
import numpy as np

def task_func(array, target_value):
    # Find the indices in the array where the first column matches the target value
    indices = np.where(array[:, 0] == target_value)[0]

    # Extract the corresponding values from the second column
    values = array[indices, 1]

    # Define the exponential decay function
    def func(x, a, b):
        return a * np.exp(-b * x)

    # Initialize the parameters
    a0 = 1
    b0 = 1

    # Perform the non-linear least squares fit
    popt, _ = optimize.curve_fit(func, values, indices, p0=[a0, b0])

    # Plot the data and the fitted function
    fig, ax = plt.subplots()
    ax.plot(values, indices, 'bo', label='Data')
    ax.plot(values, func(values, *popt), 'r-', label='Fitted function')
    ax.legend()
    ax.set_xlabel('Value')
    ax.set_ylabel('Index')
    ax.set_title('Exponential Decay Fit')

    return popt, ax
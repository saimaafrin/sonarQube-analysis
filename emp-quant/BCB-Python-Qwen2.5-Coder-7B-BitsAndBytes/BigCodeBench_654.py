
import matplotlib.pyplot as plt
import scipy.optimize as optimize
import numpy as np

def task_func(array, target_value):
    # Filter the array to include only rows where the first column matches the target value
    filtered_indices = np.where(array[:, 0] == target_value)[0]
    x_data = filtered_indices
    y_data = array[filtered_indices, 1]

    # Define the exponential decay function
    def exp_decay(x, a, b):
        return a * np.exp(-b * x)

    # Use curve_fit to fit the exponential decay function to the data
    popt, pcov = optimize.curve_fit(exp_decay, x_data, y_data)

    # Plot the original data points and the fitted curve
    fig, ax = plt.subplots()
    ax.scatter(x_data, y_data, label='Data')
    ax.plot(x_data, exp_decay(x_data, *popt), 'r-', label='Fitted Curve')

    # Add labels and legend
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    ax.legend()

    return popt, ax
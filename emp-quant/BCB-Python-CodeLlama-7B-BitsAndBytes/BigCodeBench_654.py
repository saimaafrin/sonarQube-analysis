
import matplotlib.pyplot as plt
import scipy.optimize as optimize
import numpy as np

def task_func(array, target_value):
    # Find the indices in the array where the first column matches the target value
    indices = np.where(array[:, 0] == target_value)[0]

    # Fit an exponential decay function to the indices
    popt, _ = optimize.curve_fit(lambda x, a, b: a * np.exp(-b * x), indices, array[indices, 1])

    # Plot the data and the fitted function
    fig, ax = plt.subplots()
    ax.plot(array[indices, 0], array[indices, 1], 'bo')
    ax.plot(array[indices, 0], popt[0] * np.exp(-popt[1] * array[indices, 0]), 'r-')
    ax.set_xlabel('Time')
    ax.set_ylabel('Value')
    ax.set_title('Exponential Decay Fit')
    return (popt, ax)
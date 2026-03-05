import matplotlib.pyplot as plt
import scipy.optimize as optimize
import numpy as np
def task_func(array, target_value):
    """
    Fits an exponential decay function to the indices in the array where the first column matches the target value.
    
    Parameters:
    array (np.array): A 2D numpy array where the first column represents the x-values and the second column represents the y-values.
    target_value (int): The target value to match in the first column of the array.
    
    Returns:
    tuple: A tuple containing the optimized parameters of the fitting function (popt) and the matplotlib Axes object.
    """
    # Filter the array to include only rows where the first column matches the target value
    filtered_indices = np.where(array[:, 0] == target_value)[0]
    x_values = array[filtered_indices, 0]
    y_values = array[filtered_indices, 1]
    
    # Define the exponential decay function
    def exponential_decay(x, a, b):
        return a * np.exp(-b * x)
    
    # Fit the exponential decay function to the data
    popt, pcov = optimize.curve_fit(exponential_decay, x_values, y_values)
    
    # Create a plot of the original data and the fitted curve
    fig, ax = plt.subplots()
    ax.scatter(x_values, y_values, label='Data')
    ax.plot(x_values, exponential_decay(x_values, *popt), 'r-', label='Fitted curve')
    ax.legend()
    
    return popt, ax
array = np.array([[1, 10], [2, 5], [3, 2], [4, 1], [5, 0.5], [1, 20], [2, 10], [3, 5], [4, 2], [5, 1]])
target_value = 1
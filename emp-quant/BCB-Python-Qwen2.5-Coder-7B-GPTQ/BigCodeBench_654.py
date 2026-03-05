import matplotlib.pyplot as plt
import scipy.optimize as optimize
import numpy as np
def task_func(array, target_value):
    """
    Fits an exponential decay function to the indices in the array where the first column matches the target value.
    
    Parameters:
    array (np.array): A 2D numpy array where the first column represents the indices and the second column represents the values.
    target_value (int): The target value to match in the first column of the array.
    
    Returns:
    tuple: A tuple containing the optimized parameters of the fitting function (popt) and the matplotlib Axes object.
    """
    # Filter the array to include only rows where the first column matches the target value
    filtered_indices = array[:, 0][array[:, 0] == target_value]
    filtered_values = array[:, 1][array[:, 0] == target_value]
    
    # Define the exponential decay function
    def exponential_decay(x, a, b):
        return a * np.exp(-b * x)
    
    # Initial guess for the parameters
    p0 = [1, 0.1]
    
    # Fit the exponential decay function to the filtered data
    popt, pcov = optimize.curve_fit(exponential_decay, filtered_indices, filtered_values, p0=p0)
    
    # Create a figure and axis for plotting
    fig, ax = plt.subplots()
    
    # Plot the original data
    ax.scatter(filtered_indices, filtered_values, label='Data')
    
    # Plot the fitted exponential decay function
    x_fit = np.linspace(min(filtered_indices), max(filtered_indices), 300)
    y_fit = exponential_decay(x_fit, *popt)
    ax.plot(x_fit, y_fit, 'r-', label='Fitted Exponential Decay')
    
    # Add labels and legend
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    ax.legend()
    
    return popt, ax
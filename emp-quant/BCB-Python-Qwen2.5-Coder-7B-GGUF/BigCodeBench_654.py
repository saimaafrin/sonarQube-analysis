
import matplotlib.pyplot as plt
import scipy.optimize as optimize
import numpy as np

def task_func(array, target_value):
    # Filter the array to include only rows where the first column matches the target value
    filtered_indices = np.where(array[:, 0] == target_value)[0]
    filtered_array = array[filtered_indices]
    
    # Extract the indices and the corresponding values from the filtered array
    x = filtered_indices
    y = filtered_array[:, 1]
    
    # Define the exponential decay function
    def exponential_decay(x, a, b, c):
        return a * np.exp(-b * x) + c
    
    # Use curve_fit to fit the exponential decay function to the data
    popt, pcov = optimize.curve_fit(exponential_decay, x, y)
    
    # Create a plot of the original data and the fitted curve
    fig, ax = plt.subplots()
    ax.scatter(x, y, label='Data')
    ax.plot(x, exponential_decay(x, *popt), 'r-', label='Fitted curve')
    ax.legend()
    
    return popt, ax
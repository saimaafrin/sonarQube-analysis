
import matplotlib.pyplot as plt
import scipy.optimize as optimize
import numpy as np

def task_func(array, target_value):
    # Filter the array to include only rows where the first column matches the target value
    filtered_array = array[array[:, 0] == target_value]
    
    # Extract the indices and the corresponding values from the filtered array
    indices = filtered_array[:, 1]
    values = filtered_array[:, 2]
    
    # Define the exponential decay function
    def exponential_decay(x, a, b):
        return a * np.exp(-b * x)
    
    # Use curve_fit to fit the exponential decay function to the data
    popt, pcov = optimize.curve_fit(exponential_decay, indices, values)
    
    # Create a plot of the original data and the fitted curve
    fig, ax = plt.subplots()
    ax.scatter(indices, values, label='Data')
    ax.plot(indices, exponential_decay(indices, *popt), 'r-', label='Fitted curve')
    ax.set_xlabel('Indices')
    ax.set_ylabel('Values')
    ax.legend()
    
    return popt, ax
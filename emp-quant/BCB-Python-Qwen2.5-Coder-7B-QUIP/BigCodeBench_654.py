
import matplotlib.pyplot as plt
import scipy.optimize as optimize
import numpy as np

def task_func(array, target_value):
    # Filter the array to get the rows where the first column matches the target value
    filtered_array = array[array[:, 0] == target_value]
    
    # Extract the indices and the second column values from the filtered array
    indices = filtered_array[:, 1]
    values = filtered_array[:, 2]
    
    # Define the exponential decay function
    def exp_decay(x, a, b, c):
        return a * np.exp(-b * x) + c
    
    # Initial guess for the parameters
    p0 = [1, 1, 1]
    
    # Perform the curve fitting
    popt, _ = optimize.curve_fit(exp_decay, indices, values, p0=p0)
    
    # Create a figure and an axes object
    fig, ax = plt.subplots()
    
    # Plot the original data and the fitted curve
    ax.scatter(indices, values, label='Data')
    ax.plot(indices, exp_decay(indices, *popt), 'r', label='Fitted Curve')
    
    # Add labels and legend
    ax.set_xlabel('Indices')
    ax.set_ylabel('Values')
    ax.legend()
    
    # Return the optimized parameters and the axes object
    return popt, ax
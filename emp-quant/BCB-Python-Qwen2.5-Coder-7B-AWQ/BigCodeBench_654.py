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
    filtered_array = array[array[:, 0] == target_value]
    
    # Extract the indices and values from the filtered array
    indices = filtered_array[:, 0]
    values = filtered_array[:, 1]
    
    # Define the exponential decay function
    def exponential_decay(x, a, b):
        return a * np.exp(-b * x)
    
    # Fit the exponential decay function to the indices and values
    popt, _ = optimize.curve_fit(exponential_decay, indices, values)
    
    # Create a figure and axis for plotting
    fig, ax = plt.subplots()
    
    # Plot the original data points
    ax.scatter(indices, values, label='Data')
    
    # Plot the fitted exponential decay function
    x_fit = np.linspace(min(indices), max(indices), 100)
    y_fit = exponential_decay(x_fit, *popt)
    ax.plot(x_fit, y_fit, label='Fitted Exponential Decay', color='red')
    
    # Set labels and title
    ax.set_xlabel('Indices')
    ax.set_ylabel('Values')
    ax.set_title('Exponential Decay Fit')
    ax.legend()
    
    return popt, ax
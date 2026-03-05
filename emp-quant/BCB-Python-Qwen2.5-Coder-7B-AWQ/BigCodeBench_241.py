import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
def task_func(original):
    """
    Create a numeric array from the "original" list, normalize the array, and draw the original and normalized arrays.
    
    Parameters:
    original (list): A list of numeric values.
    
    Returns:
    np.array: A numpy array for the original data.
    np.array: Normalized array.
    matplotlib.axes.Axes: Axes object with the plotted data.
    """
    # Convert the original list to a numpy array
    original_array = np.array(original)
    
    # Normalize the array using Min-Max scaling
    normalized_array = preprocessing.minmax_scale(original_array)
    
    # Create a figure and axis for plotting
    fig, ax = plt.subplots()
    
    # Plot the original and normalized arrays
    ax.plot(original_array, label='Original Data')
    ax.plot(normalized_array, label='Normalized Data')
    
    # Set the title of the plot
    ax.set_title('Original vs. Normalized Data')
    
    # Add a legend to the plot
    ax.legend()
    
    # Return the numpy arrays and the axes object
    return original_array, normalized_array, ax
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
    
    # Normalize the array using MinMaxScaler
    normalized_array = preprocessing.MinMaxScaler().fit_transform(original_array.reshape(-1, 1)).flatten()
    
    # Plotting the original and normalized arrays
    fig, ax = plt.subplots()
    ax.plot(original_array, label='Original Data')
    ax.plot(normalized_array, label='Normalized Data')
    ax.set_title('Original vs. Normalized Data')
    ax.legend()
    
    return original_array, normalized_array, ax
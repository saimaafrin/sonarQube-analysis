
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing

def task_func(original):
    # Create a numeric array from the "original" list
    original_array = np.array(original)
    
    # Normalize the array using Min-Max scaling
    normalized_array = preprocessing.minmax_scale(original_array)
    
    # Plot the original and normalized arrays
    fig, ax = plt.subplots()
    ax.plot(original_array, label='Original')
    ax.plot(normalized_array, label='Normalized')
    ax.set_title('Original vs. Normalized Data')
    ax.legend()
    
    # Return the numpy arrays and the axes object
    return original_array, normalized_array, ax
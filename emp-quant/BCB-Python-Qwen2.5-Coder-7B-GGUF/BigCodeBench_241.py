
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing

def task_func(original):
    # Convert the original list to a numpy array
    original_array = np.array(original)
    
    # Normalize the array using MinMaxScaler
    normalized_array = preprocessing.MinMaxScaler().fit_transform(original_array.reshape(-1, 1)).flatten()
    
    # Create a figure and axis for plotting
    fig, ax = plt.subplots()
    
    # Plot the original and normalized arrays
    ax.plot(original_array, label='Original Data')
    ax.plot(normalized_array, label='Normalized Data')
    
    # Add title and labels
    ax.set_title('Original vs. Normalized Data')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    
    # Add legend
    ax.legend()
    
    # Show the plot
    plt.show()
    
    # Return the numpy arrays and the axes object
    return original_array, normalized_array, ax
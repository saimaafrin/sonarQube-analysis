
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing

def task_func(original):
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
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
def task_func(original):
    # Create a numpy array from the "original" list
    original_array = np.array(original)

    # Normalize the array
    normalized_array = preprocessing.normalize(original_array)

    # Plot the original and normalized arrays
    fig, ax = plt.subplots()
    ax.plot(original_array, label='Original')
    ax.plot(normalized_array, label='Normalized')
    ax.set_title('Original vs. Normalized Data')
    ax.legend()

    return original_array, normalized_array, ax
original = [1, 2, 3, 4, 5]

import numpy as np
import matplotlib.pyplot as plt

def task_func(arr):
    # Calculate the unique values in the array
    unique_values = np.unique(arr)

    # Calculate the frequency of each unique value
    freq = np.bincount(arr)

    # Calculate the histogram of the distribution
    ax = plt.hist(unique_values, freq, np.arange(len(unique_values) + 1) - 0.5)

    # Determine if the distribution is uniform
    uniform_distribution = (len(unique_values) == 1) or (freq == freq[0])

    return (uniform_distribution, ax)
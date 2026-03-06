
import numpy as np
import matplotlib.pyplot as plt

def task_func(arr):
    # Calculate the number of unique values in the array
    unique_values = np.unique(arr)
    num_unique_values = len(unique_values)

    # Calculate the frequency of each unique value
    freq = np.zeros(num_unique_values)
    for i in range(num_unique_values):
        freq[i] = np.count_nonzero(arr == unique_values[i])

    # Calculate the probability of each unique value
    prob = freq / len(arr)

    # Check if the distribution is uniform
    uniform_distribution = True
    for i in range(num_unique_values):
        if prob[i] != 1/num_unique_values:
            uniform_distribution = False
            break

    # Generate the histogram
    ax = plt.axes()
    ax.hist(unique_values, bins=np.arange(num_unique_values + 1) - 0.5, weights=freq)
    ax.set_title('Value Distribution')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')

    return (uniform_distribution, ax)
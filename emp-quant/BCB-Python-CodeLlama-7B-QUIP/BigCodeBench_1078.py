
import numpy as np
import matplotlib.pyplot as plt

def task_func(arr):
    # Calculate the unique values in the array
    unique_values = np.unique(arr)

    # Calculate the histogram of the distribution
    hist, _ = np.histogram(arr, bins=np.arange(len(unique_values) + 1) - 0.5)

    # Determine if the distribution is uniform
    uniform_distribution = True
    for i in range(len(unique_values)):
        if hist[i] != len(arr) / len(unique_values):
            uniform_distribution = False
            break

    # Plot the histogram
    fig, ax = plt.subplots()
    ax.bar(unique_values, hist, width=1)
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    ax.set_title("Distribution of Values")

    return (uniform_distribution, ax)
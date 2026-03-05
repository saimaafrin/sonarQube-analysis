import numpy as np
import matplotlib.pyplot as plt
ARRAY_SIZE = 10000
def task_func():
    # Generate a random array of integers between 1 and 100
    array = np.random.randint(1, 100, ARRAY_SIZE)

    # Calculate the mean and standard deviation of the array
    mean = np.mean(array)
    std = np.std(array)

    # Plot the histogram of the distribution
    fig, ax = plt.subplots()
    ax.hist(array, bins=50, alpha=0.5, label='Histogram of Random Values')
    ax.set_xlabel('Val')
    ax.set_ylabel('Freq')
    ax.set_title('Histogram of Random Values')
    ax.axvline(mean, color='red', linestyle='dashed', label='Mean')
    ax.axvline(mean + std, color='purple', linestyle='dashed', label='Standard Deviation')
    ax.axvline(mean - std, color='purple', linestyle='dashed', label='Standard Deviation')
    ax.legend()

    return array, mean, std, fig
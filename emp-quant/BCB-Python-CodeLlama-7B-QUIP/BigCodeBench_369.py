
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def task_func(l):
    # Calculate the mean and standard deviation of the array
    mean = np.mean(l)
    std = np.std(l)

    # Create a histogram of the array
    n, bins, _ = plt.hist(l, 100)

    # Fit a Gaussian distribution to the histogram
    gaussian, _ = stats.norm.fit(n, bins)

    # Plot the histogram and the Gaussian fit
    ax = plt.axes()
    ax.hist(l, 100, color='blue', alpha=0.5, label='Histogram')
    ax.plot(gaussian, color='red', label='Gaussian fit')
    ax.set_xlabel('Value')
    ax.set_ylabel('Count')
    ax.set_title(f'Fit results: mu = {round(mean, 2)}, std = {round(std, 2)}')
    ax.legend()
    return ax
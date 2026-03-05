import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
def task_func(l):
    """
    Draw a histogram of the given array with a Gaussian fit.
    """
    # Calculate the mean and standard deviation of the data
    mean = np.mean(l)
    std = np.std(l)

    # Create a histogram of the data
    n, bins, patches = plt.hist(l, bins=50, facecolor='green', alpha=0.5)

    # Fit a Gaussian distribution to the data
    gaussian_fit = stats.norm(mean, std)

    # Plot the histogram with the Gaussian fit
    plt.plot(bins, gaussian_fit.pdf(bins), 'r--')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title(f'Fit results: mu = {mean:.2f},  std = {std:.2f}')
    plt.show()

    return plt.gca()
l = np.random.normal(0, 1, 100)
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
def task_func(matrix):
    """
    Calculate the distribution of the maximum values of each row in the matrix, record the histogram and the estimate of the core density of the distribution, and return the skew, kurtosis, and the histogram plot of the distribution.
    """
    # Calculate the maximum values of each row in the matrix
    max_values = np.max(matrix, axis=1)

    # Calculate the histogram of the maximum values
    hist, bins = np.histogram(max_values, bins=20)

    # Calculate the estimate of the core density of the distribution
    density = hist / np.sum(hist)

    # Calculate the skewness and kurtosis of the distribution
    skewness = stats.skew(max_values)
    kurtosis = stats.kurtosis(max_values)

    # Plot the histogram of the distribution
    fig, ax = plt.subplots()
    ax.bar(bins[:-1], hist, width=bins[1] - bins[0])
    ax.set_xlabel('Maximum value')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram of maximum values')

    return skewness, kurtosis, ax
matrix = np.random.rand(10, 10)
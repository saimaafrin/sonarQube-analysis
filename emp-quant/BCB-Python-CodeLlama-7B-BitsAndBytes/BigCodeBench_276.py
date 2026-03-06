
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def task_func(matrix):
    # Calculate the maximum values of each row in the matrix
    max_values = np.max(matrix, axis=1)

    # Calculate the histogram of the maximum values
    hist, bin_edges = np.histogram(max_values, bins=20)

    # Calculate the estimate of the core density of the distribution
    density = hist / np.sum(hist)

    # Calculate the skewness and kurtosis of the distribution
    skewness = stats.skew(max_values)
    kurtosis = stats.kurtosis(max_values)

    # Plot the histogram of the distribution
    fig, ax = plt.subplots()
    ax.bar(bin_edges[:-1], hist, width=np.diff(bin_edges), align='edge')
    ax.set_xlabel('Maximum value')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram of maximum values')

    return skewness, kurtosis, fig
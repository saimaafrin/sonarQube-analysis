
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def task_func(matrix):
    # Calculate the maximum value of each row in the matrix
    max_values = np.max(matrix, axis=1)

    # Calculate the distribution of the maximum values
    dist = stats.rv_discrete(name='max_values', values=(max_values))

    # Calculate the histogram of the distribution
    hist, bin_edges = np.histogram(dist.rvs(size=1000), bins=10)

    # Calculate the estimate of the core density of the distribution
    core_density = dist.pmf(dist.rvs(size=1000))

    # Calculate the skewness and kurtosis of the distribution
    skewness = stats.skew(dist.rvs(size=1000))
    kurtosis = stats.kurtosis(dist.rvs(size=1000))

    # Plot the histogram of the distribution
    fig, ax = plt.subplots()
    ax.bar(bin_edges[:-1], hist, width=bin_edges[1] - bin_edges[0])
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram of the distribution')

    return skewness, kurtosis, ax
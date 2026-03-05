import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
def task_func(matrix):
    # Calculate the distribution of the maximum values of each row in the matrix
    max_vals = np.max(matrix, axis=1)
    hist, bins = np.histogram(max_vals, bins=20)
    density = hist / (bins[1] - bins[0])

    # Calculate the skewness and kurtosis of the distribution
    skewness = stats.skew(max_vals)
    kurtosis = stats.kurtosis(max_vals)

    # Plot the histogram of the distribution
    fig, ax = plt.subplots()
    ax.bar(bins[:-1], density, width=bins[1] - bins[0])
    ax.set_xlabel('Maximum value')
    ax.set_ylabel('Density')
    ax.set_title('Histogram of the distribution')

    return skewness, kurtosis, ax
matrix = np.random.rand(10, 10)
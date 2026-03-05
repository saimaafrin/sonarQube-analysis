
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def task_func(matrix):
    # Calculate the maximum value of each row in the matrix
    max_values = np.max(matrix, axis=1)

    # Calculate the distribution of the maximum values
    hist, edges = np.histogram(max_values, bins=50)
    density = hist / np.sum(hist)

    # Calculate the skewness and kurtosis of the distribution
    skewness = stats.skewness(max_values)
    kurtosis = stats.kurtosis(max_values)

    # Plot the histogram
    fig, ax = plt.subplots()
    ax.hist(max_values, bins=50, label="Histogram")
    ax.set_xlabel("Maximum value")
    ax.set_ylabel("Frequency")
    ax.set_title("Distribution of maximum values")
    ax.legend()

    return skewness, kurtosis, fig
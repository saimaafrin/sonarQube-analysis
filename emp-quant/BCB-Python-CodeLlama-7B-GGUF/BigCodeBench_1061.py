
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def task_func(arr: np.ndarray) -> (plt.Axes, np.ndarray):
    # Calculate the sum of elements in each row of the array
    row_sums = arr.sum(axis=1)

    # Calculate the mean and standard deviation of the row sums
    mean = row_sums.mean()
    std = row_sums.std()

    # Normalize the row sums by subtracting the mean and dividing by the standard deviation
    normalized_row_sums = (row_sums - mean) / std

    # If the standard deviation is 0, normalization results in an array of zeros with the same shape
    if std == 0:
        normalized_row_sums = np.zeros_like(row_sums)

    # Create a histogram of the normalized data
    hist, bins = np.histogram(normalized_row_sums, bins=30, density=True)

    # Create a matplotlib Axes object with the histogram and the overlaid standard normal PDF
    fig, ax = plt.subplots()
    ax.bar(bins[:-1], hist, width=bins[1] - bins[0], alpha=0.6, color='g')
    ax.plot(norm.pdf(bins, loc=mean, scale=std), color='r', linewidth=2)
    ax.set_title('Histogram of Normalized Data with Standard Normal PDF')

    return ax, normalized_row_sums
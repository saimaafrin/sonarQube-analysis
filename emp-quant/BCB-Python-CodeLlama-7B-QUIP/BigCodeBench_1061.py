
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def task_func(arr: np.ndarray) -> (plt.Axes, np.ndarray):
    # Calculate the mean and standard deviation of the row sums
    mean = np.mean(arr, axis=1)
    std = np.std(arr, axis=1)

    # Normalize the row sums by subtracting the mean and dividing by the standard deviation
    norm_arr = (arr - mean) / std

    # Plot a histogram of the normalized data
    fig, ax = plt.subplots()
    ax.hist(norm_arr, bins=30, alpha=0.6, facecolor='green', edgecolor='green')
    ax.set_xlabel('Normalized data')
    ax.set_ylabel('Probability')
    ax.set_title('Histogram of Normalized Data with Standard Normal PDF')

    # Overlay the standard normal PDF on the histogram
    x = np.linspace(norm.ppf(0.001, 0, 1), norm.ppf(0.999, 0, 1), 100)
    y = norm.pdf(x)
    ax.plot(x, y, color='red', linewidth=2)

    return (ax, norm_arr)
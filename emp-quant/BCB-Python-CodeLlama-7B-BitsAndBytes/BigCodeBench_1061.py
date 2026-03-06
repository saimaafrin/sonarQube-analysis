
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def task_func(arr: np.ndarray) -> (plt.Axes, np.ndarray):
    # Calculate the mean and standard deviation of the row sums
    mean = arr.sum(axis=1).mean()
    std = arr.sum(axis=1).std()

    # Normalize the row sums by subtracting the mean and dividing by the standard deviation
    norm_arr = (arr.sum(axis=1) - mean) / std

    # Create a histogram of the normalized data
    hist, bins = np.histogram(norm_arr, bins=30, density=True)
    hist = hist / hist.sum() * 0.6
    hist = np.ma.masked_where(hist == 0, hist)

    # Create a plot of the histogram and the standard normal PDF
    fig, ax = plt.subplots()
    ax.bar(bins[:-1], hist, alpha=0.6, color='green')
    x = np.linspace(bins[0], bins[-1], 1000)
    y = norm.pdf(x, loc=mean, scale=std)
    ax.plot(x, y, color='red', linewidth=2)
    ax.set_title('Histogram of Normalized Data with Standard Normal PDF')

    return ax, norm_arr
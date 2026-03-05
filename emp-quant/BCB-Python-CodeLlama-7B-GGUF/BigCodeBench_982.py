
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def task_func(df, column, bins=30, density=True, alpha=0.6, color="g", seed=None):
    # Calculate the histogram
    counts, bins = np.histogram(df[column], bins=bins, density=density)

    # Calculate the mean and standard deviation of the histogram
    mean = np.mean(df[column])
    std = np.std(df[column])

    # Calculate the fitted normal distribution parameters
    mu = mean
    sigma = std
    x = np.linspace(bins[0], bins[-1], 100)
    y = norm.pdf(x, mu, sigma)

    # Plot the histogram and the fitted normal distribution
    ax = plt.axes()
    ax.bar(bins[:-1], counts, width=bins[1]-bins[0], alpha=alpha, color=color)
    ax.plot(x, y, color="r")
    ax.set_xlabel(column)
    ax.set_ylabel("Frequency")
    ax.set_title("Histogram of {}".format(column))
    return ax
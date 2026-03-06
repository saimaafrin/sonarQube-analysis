
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def task_func(df, column, bins=30, density=True, alpha=0.6, color="g", seed=None):
    # Calculate the histogram of the specified column
    counts, bin_edges = np.histogram(df[column], bins=bins, density=density)

    # Calculate the mean and standard deviation of the histogram
    mean = np.mean(df[column])
    std = np.std(df[column])

    # Calculate the fitted normal distribution curve
    x = np.linspace(bin_edges[0], bin_edges[-1], 100)
    y = norm.pdf(x, mean, std)

    # Plot the histogram and fitted normal distribution curve
    fig, ax = plt.subplots()
    ax.bar(bin_edges[:-1], counts, alpha=alpha, color=color)
    ax.plot(x, y, color="r")
    ax.set_xlabel(column)
    ax.set_ylabel("Frequency")
    ax.set_title("Histogram of {}".format(column))
    return ax
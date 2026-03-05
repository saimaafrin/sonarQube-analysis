
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def task_func(df, column, bins=30, density=True, alpha=0.6, color="g", seed=None):
    # Calculate the histogram of the specified column
    counts, bin_edges = np.histogram(df[column], bins=bins, density=density)

    # Calculate the normal distribution curve
    mean = np.mean(df[column])
    std = np.std(df[column])
    x = np.linspace(bin_edges[0], bin_edges[-1], 100)
    y = norm.pdf(x, mean, std)

    # Plot the histogram and the normal distribution curve
    ax = plt.subplot(111)
    ax.hist(df[column], bins=bins, alpha=alpha, color=color, label="Histogram")
    ax.plot(x, y, label="Normal Distribution")
    ax.set_xlabel("Value")
    ax.set_ylabel("Count")
    ax.set_title("Histogram of the specified column")
    ax.legend()
    return ax
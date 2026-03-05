import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
def task_func(length):
    """
    Create a normal distribution with a given length, plot its histogram alongside the probability density function, and return the distribution and the plot.
    """
    # Generate a normal distribution with mean 0 and standard deviation 1
    distribution = norm.rvs(size=length)

    # Create a histogram of the distribution
    hist, bins = np.histogram(distribution, bins=50)

    # Create a plot of the histogram and the probability density function
    fig, ax = plt.subplots()
    ax.bar(bins[:-1], hist, width=bins[1] - bins[0])
    ax.plot(bins, norm.pdf(bins), label='Probability density function')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram of a normal distribution')
    ax.legend()

    return distribution, fig
length = 1000
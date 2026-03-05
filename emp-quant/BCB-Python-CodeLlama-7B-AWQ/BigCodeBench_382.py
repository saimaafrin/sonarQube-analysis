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
    hist, bins = np.histogram(distribution, bins='auto')

    # Create a plot of the histogram and the probability density function
    fig, ax = plt.subplots()
    ax.bar(bins[:-1], hist, width=np.diff(bins), align='edge', alpha=0.5)
    ax.plot(bins, norm.pdf(bins), 'r--')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram of Normal Distribution')

    return distribution, fig
length = 1000
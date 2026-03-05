import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
def task_func(length):
    """
    Create a normal distribution with a given length, plot its histogram alongside the probability density function, and return the distribution and the plot.
    """
    # Generate a normal distribution with mean 0 and standard deviation 1
    distribution = norm.rvs(size=length)

    # Plot the histogram of the distribution
    fig, ax = plt.subplots()
    ax.hist(distribution, bins=50, alpha=0.5, label='Histogram')

    # Plot the probability density function of the distribution
    ax.plot(distribution, label='Probability Density Function')

    # Add labels and title to the plot
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title('Normal Distribution')
    ax.legend()

    # Return the distribution and the plot
    return distribution, fig
length = 1000
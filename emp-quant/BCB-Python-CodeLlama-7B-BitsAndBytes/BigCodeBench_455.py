
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def task_func(mean, std_dev, n):
    # Generate n samples from a normal distribution with mean and standard deviation
    samples = stats.norm.rvs(mean, std_dev, size=n)
    # Plot the histogram of the samples
    plt.hist(samples, bins=50, density=True, alpha=0.5, label='Histogram of Samples')
    # Plot the probability density function of the normal distribution
    x = np.linspace(mean - 3 * std_dev, mean + 3 * std_dev, 1000)
    plt.plot(x, stats.norm.pdf(x, mean, std_dev), label='Probability Density Function')
    plt.legend()
    plt.show()
    return samples
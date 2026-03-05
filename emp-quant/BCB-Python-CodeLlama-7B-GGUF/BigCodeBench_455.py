
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def task_func(mean, std_dev, n):
    # Generate a set of samples from a normal distribution
    samples = stats.norm.rvs(mean, std_dev, size=n)
    # Plot the histogram of the samples
    plt.hist(samples, bins=50)
    # Plot the probability density function of the normal distribution
    x = np.linspace(mean - 3 * std_dev, mean + 3 * std_dev, 1000)
    plt.plot(x, stats.norm.pdf(x, mean, std_dev))
    plt.xlabel('Value')
    plt.ylabel('Probability')
    plt.title('Normal Distribution with Mean = {}, Std Dev = {}'.format(mean, std_dev))
    plt.show()
    return samples
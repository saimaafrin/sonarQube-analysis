import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
def task_func(mean, std_dev, n):
    """
    Generates a set of samples from a normal distribution with a specified mean and standard deviation.
    It also visualizes the generated samples by plotting their histogram and the probability density function.
    """
    # Generate samples from the normal distribution
    samples = stats.norm.rvs(mean, std_dev, size=n)

    # Plot the histogram of the samples
    plt.hist(samples, bins=50, alpha=0.5, label='Samples')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram of Samples')
    plt.legend()
    plt.show()

    # Plot the probability density function of the normal distribution
    x = np.linspace(mean - 3 * std_dev, mean + 3 * std_dev, 1000)
    y = stats.norm.pdf(x, mean, std_dev)
    plt.plot(x, y, label='Probability Density Function')
    plt.xlabel('Value')
    plt.ylabel('Probability')
    plt.title('Probability Density Function of the Normal Distribution')
    plt.legend()
    plt.show()

    return samples
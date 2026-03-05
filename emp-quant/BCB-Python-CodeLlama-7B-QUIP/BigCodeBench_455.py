
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def task_func(mean, std_dev, n):
    # Generate samples from a normal distribution
    samples = stats.norm.rvs(mean, std_dev, size=n)
    # Plot the histogram of the samples
    plt.hist(samples, bins=50, alpha=0.5, label='Histogram of generated samples')
    # Plot the probability density function of the normal distribution
    x = np.linspace(0, 10, 1000)
    plt.plot(x, stats.norm.pdf(x, mean, std_dev), label='Probability density function of the normal distribution')
    plt.legend()
    plt.show()
    return samples

# Generate 500 samples from a normal distribution with mean 5 and standard deviation 2
samples = task_func(5, 2, 500)

# Print the first 10 samples
print(samples[:10])
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
def task_func(mu, sigma, num_samples):
    """
    Generate a plot showing a normal distribution with a given mean and standard deviation and overlay a histogram of randomly generated samples from this distribution.
    """
    # Generate a normal distribution with the given mean and standard deviation
    x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)
    y = stats.norm.pdf(x, mu, sigma)

    # Generate a histogram of randomly generated samples from the normal distribution
    samples = stats.norm.rvs(mu, sigma, size=num_samples)
    hist, bins = np.histogram(samples, bins=50)

    # Plot the normal distribution and the histogram
    fig, ax = plt.subplots()
    ax.plot(x, y, label='Normal distribution')
    ax.bar(bins[:-1], hist, width=np.diff(bins), label='Histogram of samples')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title('Normal Distribution')
    ax.legend()

    return fig
mu = 0
sigma = 1
num_samples = 1000
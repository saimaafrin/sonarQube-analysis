import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
def task_func(mu, sigma, num_samples):
    # Generate a normal distribution with the given mean and standard deviation
    dist = stats.norm(mu, sigma)

    # Generate a set of random samples from the distribution
    samples = dist.rvs(size=num_samples)

    # Create a histogram of the samples
    hist, _ = np.histogram(samples, bins=20)

    # Create a figure with the normal distribution and the histogram
    fig, ax = plt.subplots()
    ax.plot(dist.pdf(x), label='Normal Distribution')
    ax.bar(hist, label='Histogram of Samples')
    ax.set_title('Normal Distribution')
    ax.legend()

    return fig
mu = 0
sigma = 1
num_samples = 1000
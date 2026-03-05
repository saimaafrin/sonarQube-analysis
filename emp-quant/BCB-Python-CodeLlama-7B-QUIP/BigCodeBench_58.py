
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def task_func(mu, sigma, num_samples):
    # Generate a normal distribution
    dist = stats.norm(mu, sigma)

    # Generate random samples from the distribution
    samples = dist.rvs(size=num_samples)

    # Plot the histogram of the samples
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.hist(samples, bins=50, alpha=0.5, label='Samples')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title('Normal Distribution')
    ax.legend()

    return fig
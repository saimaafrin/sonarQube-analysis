
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def task_func(mu=0, sigma=1, sample_size=1000, seed=0):
    # Generate a sample from a normal distribution
    np.random.seed(seed)
    x = np.random.normal(mu, sigma, sample_size)

    # Calculate the empirical mean and standard deviation of the sample
    mean = np.mean(x)
    std = np.std(x)

    # Plot the histogram and the probability density function
    fig, ax = plt.subplots()
    ax.hist(x, bins=50, density=True, alpha=0.5, label='Sample')
    ax.plot(x, stats.norm.pdf(x, mu, sigma), label='Normal PDF')
    ax.set_title(f'Normal Distribution with $\\mu = {mu:.2f}, \\sigma = {sigma:.2f}$')
    ax.legend()
    ax.set_xlabel('Value')
    ax.set_ylabel('Probability')
    plt.show()

    return ax, mean, std
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
def task_func(length):
    """
    Create a normal distribution with a given length, plot its histogram alongside the probability density function,
    and return the distribution and the plot.

    Parameters:
    length (int): The number of samples in the normal distribution.

    Returns:
    tuple: A tuple containing:
        1. numpy array with the normal distribution.
        2. matplotlib Axes object representing the plot.
    """
    # Generate the normal distribution
    mu = 0
    sigma = 1
    distribution = norm.rvs(mu, sigma, length)

    # Create the plot
    fig, ax = plt.subplots()
    ax.hist(distribution, bins=30, density=True, alpha=0.6, color='g')
    ax.plot(np.linspace(mu - 3*sigma, mu + 3*sigma, 100), norm.pdf(np.linspace(mu - 3*sigma, mu + 3*sigma, 100), mu, sigma), 'r-', lw=2)
    ax.set_title('Normal Distribution')
    ax.set_xlabel('Value')
    ax.set_ylabel('Probability Density')

    return distribution, ax
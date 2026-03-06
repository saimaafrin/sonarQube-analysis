import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
def task_func(mu, sigma, num_samples):
    """
    Display a plot showing a normal distribution with a given mean and standard deviation and overlay a histogram of randomly generated samples from this distribution.
    The plot title should be 'Normal Distribution'.

    Parameters:
    mu (float): The mean of the distribution.
    sigma (float): The standard deviation of the distribution.
    num_samples (int): The number of samples to generate.

    Returns:
    fig (matplotlib.figure.Figure): The generated figure. Useful for testing purposes.

    Requirements:
    - numpy
    - scipy.stats
    - matplotlib.pyplot

    Example:
    >>> plt = task_func(0, 1, 1000)
    """
    # Generate samples from the distribution
    samples = stats.norm.rvs(mu, sigma, num_samples)

    # Plot the distribution
    fig = plt.figure()
    plt.title('Normal Distribution')
    plt.plot(stats.norm.pdf(np.linspace(-5, 5, 100), mu, sigma))
    plt.hist(samples, bins=100, density=True)
    plt.show()

    return fig
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
def task_func(n_samples=1000, mu=0, sigma=1, random_seed=0):
    """
    Generates a histogram and a probability density function (PDF) plot for a specified normal distribution.

    This function draws n_samples from a normal distribution defined by mean (mu) and standard deviation (sigma),
    plots a histogram of the samples, and overlays the PDF of the normal distribution. The histogram's density
    is normalized, and the PDF is plotted with a red line with linewidth=2.

    Parameters:
    - n_samples (int): Number of samples for the histogram. Must be greater than 0. Default is 1000.
    - mu (float): Mean for the normal distribution. Default is 0.
    - sigma (float): Standard deviation for the normal distribution. Must be greater than 0. Default is 1.
    - random_seed (int): Random seed for reproducibility. Defaults to 0.

    Returns:
    - ax (matplotlib.axes._axes.Axes): Axes object with the histogram and PDF plotted.
    - samples (numpy.ndarray): Generated sample data.

    Requirements:
    - numpy
    - matplotlib.pyplot
    - scipy.stats.norm

    Example:
    >>> ax, samples = task_func()
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    >>> ax.get_xticklabels()
    [Text(-5.0, 0, '−5'), Text(-4.0, 0, '−4'), Text(-3.0, 0, '−3'), Text(-2.0, 0, '−2'), Text(-1.0, 0, '−1'), Text(0.0, 0, '0'), Text(1.0, 0, '1'), Text(2.0, 0, '2'), Text(3.0, 0, '3'), Text(4.0, 0, '4'), Text(5.0, 0, '5')]
    """
    # Set random seed for reproducibility
    np.random.seed(random_seed)

    # Generate samples from the normal distribution
    samples = norm.rvs(loc=mu, scale=sigma, size=n_samples)

    # Plot the histogram and the PDF
    ax = plt.hist(samples, bins=10, density=True, color='#0072B2', alpha=0.5)
    plt.plot(samples, norm.pdf(samples, loc=mu, scale=sigma), color='#D50000', linewidth=2)

    return ax, samples
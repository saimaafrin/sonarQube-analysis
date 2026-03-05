import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
def task_func(n_samples=1000, mu=0, sigma=1, random_seed=0):
    """
    Generates a histogram and a probability density function (PDF) plot for a specified normal distribution.
    This function draws n_samples from a normal distribution defined by mean (mu) and standard deviation (sigma),
    plots a histogram of the samples, and overlays the PDF of the normal distribution.
    The histogram's density is normalized, and the PDF is plotted with a red line with linewidth=2.
    The function should output with:
        ax (matplotlib.axes._axes.Axes): Axes object with the histogram and PDF plotted.
        samples (numpy.ndarray): Generated sample data.
    """
    # Set random seed for reproducibility
    np.random.seed(random_seed)

    # Generate samples from the normal distribution
    samples = np.random.normal(mu, sigma, n_samples)

    # Create a histogram of the samples
    ax = plt.hist(samples, bins=50, density=True, alpha=0.5, label='Histogram')

    # Overlay the PDF of the normal distribution
    x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)
    y = norm.pdf(x, mu, sigma)
    ax.plot(x, y, color='red', linewidth=2, label='PDF')

    # Set the x-axis label and legend
    ax.set_xlabel('Value')
    ax.legend()

    return ax, samples
n_samples = 1000
mu = 0
sigma = 1
random_seed = 0
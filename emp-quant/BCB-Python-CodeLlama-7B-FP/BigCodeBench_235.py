import numpy as np
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
def task_func(mu, sigma, seed=0, num_samples=1000, num_bins=30):
    """
    Create a histogram of a normal distribution with a given mean and standard deviation,
    and overlay the probability density function (PDF) of the normal distribution on the histogram.
    Additionally, overlay a second order polynomial function on the histogram fitted bin-wise using ordinary least squares (OLS) regression.
    The random seed is set for reproducibility.
    The color of the PDF line is red, and the color of the OLS line is green.
    """
    # Set random seed for reproducibility
    np.random.seed(seed)

    # Generate random samples from a normal distribution
    samples = np.random.normal(mu, sigma, num_samples)

    # Create histogram of samples
    hist, bins = np.histogram(samples, num_bins, density=True)

    # Normalize histogram
    hist = hist / hist.sum()

    # Plot histogram
    ax = plt.axes()
    ax.bar(bins[:-1], hist, width=bins[1] - bins[0], alpha=0.5, color='C0')

    # Overlay PDF of normal distribution
    x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 1000)
    y = np.exp(-((x - mu) ** 2) / (2 * sigma ** 2)) / (sigma * np.sqrt(2 * np.pi))
    ax.plot(x, y, color='red', label='PDF')

    # Fit second order polynomial function to histogram
    x = np.linspace(bins[0], bins[-1], num_bins)
    y = hist
    model = ols('y ~ x**2', data=dict(x=x, y=y)).fit()
    ax.plot(x, model.predict(x), color='green', label='OLS')

    # Set axis labels and legend
    ax.set_xlabel('Value')
    ax.set_ylabel('Density')
    ax.legend()

    return ax
mu = 0
sigma = 1
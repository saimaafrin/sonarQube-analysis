import numpy as np
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
def task_func(mu, sigma, seed=0, num_samples=1000, num_bins=30):
    # Set random seed for reproducibility
    np.random.seed(seed)

    # Generate random samples from a normal distribution
    samples = np.random.normal(mu, sigma, num_samples)

    # Create a histogram of the samples
    hist, bins = np.histogram(samples, bins=num_bins)

    # Overlay the probability density function (PDF) of the normal distribution on the histogram
    pdf = np.exp(-((bins - mu) ** 2) / (2 * sigma ** 2)) / (sigma * np.sqrt(2 * np.pi))
    plt.plot(bins, pdf, color='red')

    # Overlay a second order polynomial function on the histogram fitted bin-wise using ordinary least squares (OLS) regression
    x = np.linspace(bins[0], bins[-1], num_bins)
    y = np.polyfit(bins, hist, 2)
    plt.plot(x, y, color='green')

    # Return the Axes object with the histogram and overlaid PDF
    return plt.gca()
mu = 0
sigma = 1
seed = 0
num_samples = 1000
num_bins = 30
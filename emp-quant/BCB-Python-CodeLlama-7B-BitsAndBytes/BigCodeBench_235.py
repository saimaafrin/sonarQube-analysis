
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

    # Normalize the histogram
    hist = hist / hist.sum()

    # Plot the histogram
    ax = plt.axes()
    ax.bar(bins[:-1], hist, width=bins[1] - bins[0], align='edge')
    ax.set_xlabel('Value')
    ax.set_ylabel('Probability')
    ax.set_title('Histogram of Normal Distribution')

    # Overlay the PDF of the normal distribution
    x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 1000)
    y = np.exp(-((x - mu) ** 2) / (2 * sigma ** 2)) / (sigma * np.sqrt(2 * np.pi))
    ax.plot(x, y, color='red')

    # Overlay the OLS fit of the normal distribution
    x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 1000)
    y = np.exp(-((x - mu) ** 2) / (2 * sigma ** 2)) / (sigma * np.sqrt(2 * np.pi))
    model = ols('y ~ x', data=dict(x=x, y=y)).fit()
    ax.plot(x, model.predict(x), color='green')

    return ax
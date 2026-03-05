import numpy as np
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
def task_func(mu, sigma, seed=0, num_samples=1000, num_bins=30):
    """
    Create a histogram of a normal distribution with a given mean and standard deviation,
    and overlay the probability density function (PDF) of the normal distribution on the histogram.
    Additionally, overlay a second order polynomial function on the histogram fitted bin-wise using ordinary least squares (OLS) regression.
    The random seed is set for reproducibility. The color of the PDF line is red, and the color of the OLS line is green.
    """
    # Set random seed for reproducibility
    np.random.seed(seed)

    # Generate random samples from a normal distribution
    samples = np.random.normal(mu, sigma, num_samples)

    # Create histogram of samples
    hist, bin_edges = np.histogram(samples, bins=num_bins)

    # Normalize histogram
    hist = hist / np.sum(hist)

    # Create x-axis values for the histogram
    x_values = np.linspace(bin_edges[0], bin_edges[-1], num_bins)

    # Plot histogram
    ax = plt.axes()
    ax.bar(x_values, hist, width=np.diff(bin_edges)[0], align='edge', alpha=0.5)

    # Plot PDF of normal distribution
    x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 1000)
    y = np.exp(-((x - mu) ** 2) / (2 * sigma ** 2)) / (sigma * np.sqrt(2 * np.pi))
    ax.plot(x, y, color='red', label='PDF')

    # Fit a second order polynomial function to the histogram
    x_data = x_values[hist > 0]
    y_data = hist[hist > 0]
    model = ols('y ~ x + I(x ** 2)', data=pd.DataFrame({'x': x_data, 'y': y_data}))
    model_fit = model.fit()
    x_fit = np.linspace(x_data.min(), x_data.max(), 1000)
    y_fit = model_fit.predict(pd.DataFrame({'x': x_fit}))
    ax.plot(x_fit, y_fit, color='green', label='OLS fit')

    # Set axis labels and title
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram of Normal Distribution with OLS Fit')

    # Return the Axes object with the histogram and overlaid PDF
    return ax
mu = 0
sigma = 1
seed = 0
num_samples = 1000
num_bins = 30
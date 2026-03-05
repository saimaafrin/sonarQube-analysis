import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from statsmodels.formula.api import ols
def task_func(mu, sigma, seed=0, num_samples=1000, num_bins=30):
    """
    Create a histogram of a normal distribution with a given mean and standard deviation,
    and overlay the probability density function (PDF) of the normal distribution on the histogram.
    Additionally, overlay a second order polynomial function on the histogram fitted bin-wise using
    ordinary least squares (OLS) regression. The random seed is set for reproducibility.
    The color of the PDF line is red, and the color of the OLS line is green.
    
    Parameters:
    - mu: Mean of the normal distribution.
    - sigma: Standard deviation of the normal distribution.
    - seed: Seed for the random number generator for reproducibility.
    - num_samples: Number of samples to generate from the normal distribution.
    - num_bins: Number of bins for the histogram.
    
    Returns:
    - matplotlib.axes.Axes: The Axes object with the histogram and overlaid PDF.
    """
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Generate samples from the normal distribution
    samples = np.random.normal(mu, sigma, num_samples)
    
    # Create a histogram of the samples
    fig, ax = plt.subplots()
    ax.hist(samples, bins=num_bins, density=True, alpha=0.6, color='g')
    
    # Calculate the PDF of the normal distribution
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
    pdf = norm.pdf(x, mu, sigma)
    ax.plot(x, pdf, 'r-', lw=2)
    
    # Fit a second order polynomial to the histogram bins
    bin_edges = np.histogram_bin_edges(samples, bins=num_bins)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
    bin_counts = np.histogram(samples, bins=bin_edges)[0]
    bin_counts = bin_counts / bin_counts.sum()  # Normalize counts to get probabilities
    
    # Create a DataFrame for OLS regression
    df = pd.DataFrame({'x': bin_centers, 'y': bin_counts})
    
    # Fit a second order polynomial
    model = ols('y ~ x + I(x**2)', data=df).fit()
    x_poly = np.linspace(bin_centers.min(), bin_centers.max(), 100)
    y_poly = model.predict(pd.DataFrame({'x': x_poly, 'I(x**2)': x_poly**2}))
    
    # Plot the polynomial fit
    ax.plot(x_poly, y_poly, 'g-', lw=2)
    
    return ax
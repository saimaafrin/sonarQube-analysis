import numpy as np
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
def task_func(mu, sigma, seed=0, num_samples=1000, num_bins=30):
    """
    Plots a histogram of a normal distribution with a given mean and standard deviation,
    overlays the probability density function (PDF) of the normal distribution, and overlays
    a second order polynomial function fitted bin-wise using ordinary least squares (OLS) regression.
    
    Parameters:
    - mu: Mean of the normal distribution.
    - sigma: Standard deviation of the normal distribution.
    - seed: Seed for random number generator for reproducibility.
    - num_samples: Number of samples to generate.
    - num_bins: Number of bins for the histogram.
    
    Returns:
    - matplotlib.axes.Axes: The Axes object with the histogram and overlaid PDF.
    """
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Generate samples from a normal distribution
    samples = np.random.normal(mu, sigma, num_samples)
    
    # Create a histogram of the samples
    ax = plt.hist(samples, bins=num_bins, density=True, alpha=0.6, color='g')
    
    # Generate x values for the PDF
    x = np.linspace(min(samples), max(samples), 100)
    
    # Calculate the PDF values
    pdf = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
    
    # Plot the PDF
    ax.plot(x, pdf, 'r-', lw=2)
    
    # Fit a second order polynomial using OLS regression
    bin_edges = np.linspace(min(samples), max(samples), num_bins + 1)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
    bin_counts = np.histogram(samples, bins=bin_edges)[0]
    
    # Create a design matrix for the polynomial regression
    X = np.column_stack((bin_centers**2, bin_centers, np.ones_like(bin_centers)))
    
    # Fit the model using OLS
    model = ols('bin_counts ~ bin_centers**2 + bin_centers + 1', data={'bin_counts': bin_counts, 'bin_centers': bin_centers}).fit()
    
    # Predict the values using the fitted model
    y_pred = model.predict(X)
    
    # Plot the OLS line
    ax.plot(bin_centers, y_pred, 'g-', lw=2)
    
    return ax
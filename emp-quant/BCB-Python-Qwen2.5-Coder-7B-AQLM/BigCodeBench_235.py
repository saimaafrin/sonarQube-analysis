
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols

def task_func(mu, sigma, seed=0, num_samples=1000, num_bins=30):
    np.random.seed(seed)
    data = np.random.normal(mu, sigma, num_samples)
    
    # Create histogram
    ax = plt.hist(data, bins=num_bins, density=True, alpha=0.6, color='g')
    
    # Overlay PDF of normal distribution
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
    y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * (x - mu) ** 2 / sigma ** 2)
    ax.plot(x, y, 'r-', lw=2)
    
    # Fit second order polynomial using OLS regression
    bin_edges = np.histogram_bin_edges(data, bins=num_bins)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
    bin_counts = np.histogram(data, bins=bin_edges)[0]
    bin_counts = bin_counts[bin_counts > 0]  # Avoid division by zero
    bin_centers = bin_centers[bin_counts > 0]
    
    # Create a design matrix for the polynomial
    X = np.column_stack((bin_centers**2, bin_centers, np.ones_like(bin_centers)))
    
    # Fit the polynomial using OLS
    model = ols('bin_counts ~ bin_centers**2 + bin_centers + 1', data={'bin_counts': bin_counts, 'bin_centers': bin_centers}).fit()
    y_ols = model.predict(X)
    
    # Overlay the OLS polynomial
    ax.plot(bin_centers, y_ols, 'g-', lw=2)
    
    return ax
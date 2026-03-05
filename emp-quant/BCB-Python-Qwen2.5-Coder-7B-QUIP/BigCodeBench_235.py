
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols

def task_func(mu, sigma, seed=0, num_samples=1000, num_bins=30):
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Generate data from a normal distribution
    data = np.random.normal(mu, sigma, num_samples)
    
    # Create a histogram of the data
    fig, ax = plt.subplots()
    ax.hist(data, bins=num_bins, density=True, alpha=0.6)
    
    # Calculate the bin edges
    bin_edges = ax.get_xdata()
    
    # Calculate the bin centers
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
    
    # Fit a second order polynomial to the data using OLS regression
    x = bin_centers
    y = np.histogram(data, bins=bin_edges)[0]
    model = ols('y ~ x + I(x**2)', data={'x': x, 'y': y})
    results = model.fit()
    
    # Evaluate the polynomial at the bin centers
    y_poly = results.predict({'x': bin_centers})
    
    # Overlay the PDF of the normal distribution
    ax.plot(bin_centers, (1/(sigma * np.sqrt(2 * np.pi))) * np.exp(-(bin_centers - mu)**2 / (2 * sigma**2)), 'r', lw=2)
    
    # Overlay the polynomial function
    ax.plot(bin_centers, y_poly, 'g', lw=2)
    
    # Return the Axes object
    return ax
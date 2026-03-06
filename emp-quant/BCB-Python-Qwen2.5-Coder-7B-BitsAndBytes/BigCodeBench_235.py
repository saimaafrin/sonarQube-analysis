
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols

def task_func(mu, sigma, seed=0, num_samples=1000, num_bins=30):
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Generate samples from a normal distribution
    data = np.random.normal(mu, sigma, num_samples)
    
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Plot the histogram of the data
    n, bins, patches = ax.hist(data, bins=num_bins, density=True, alpha=0.6, color='g')
    
    # Calculate the midpoint of each bin
    bin_centers = 0.5 * (bins[:-1] + bins[1:])
    
    # Fit a second order polynomial to the histogram data using OLS
    model = ols('n ~ C(bin_centers) + I(bin_centers**2)', data={'bin_centers': bin_centers, 'n': n}).fit()
    
    # Evaluate the polynomial at the bin centers
    y_ols = model.predict({'bin_centers': bin_centers})
    
    # Plot the polynomial fit
    ax.plot(bin_centers, y_ols, 'r-', label='Polynomial Fit')
    
    # Plot the PDF of the normal distribution
    x_pdf = np.linspace(min(data), max(data), 100)
    y_pdf = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x_pdf - mu) / sigma) ** 2)
    ax.plot(x_pdf, y_pdf, 'r--', label='Normal PDF')
    
    # Add labels and legend
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.legend()
    
    return ax
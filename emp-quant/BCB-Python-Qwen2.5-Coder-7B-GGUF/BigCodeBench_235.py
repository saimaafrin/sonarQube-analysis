
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols

def task_func(mu, sigma, seed=0, num_samples=1000, num_bins=30):
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Generate samples from a normal distribution
    samples = np.random.normal(mu, sigma, num_samples)
    
    # Create a histogram of the samples
    counts, bin_edges = np.histogram(samples, bins=num_bins, density=True)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
    
    # Plot the histogram
    fig, ax = plt.subplots()
    ax.bar(bin_centers, counts, width=np.diff(bin_edges), align='center', alpha=0.7)
    
    # Plot the PDF of the normal distribution
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
    pdf = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
    ax.plot(x, pdf, 'r-', label='PDF')
    
    # Fit a second order polynomial using OLS regression
    data = np.column_stack((bin_centers**2, bin_centers, np.ones_like(bin_centers)))
    model = ols('counts ~ bin_centers**2 + bin_centers + 1', data=data).fit()
    y_ols = model.predict(data)
    
    # Plot the OLS line
    ax.plot(bin_centers, y_ols, 'g-', label='OLS')
    
    # Add labels and legend
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.legend()
    
    return ax
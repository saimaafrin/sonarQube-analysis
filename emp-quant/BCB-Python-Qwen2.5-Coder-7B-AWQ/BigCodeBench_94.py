import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
def task_func(mean, std_dev, num_samples):
    # Generate samples from a normal distribution
    samples = np.random.normal(mean, std_dev, num_samples)
    
    # Create a figure and axis for plotting
    fig, ax = plt.subplots()
    
    # Plot the histogram of the samples
    n, bins, patches = ax.hist(samples, bins=30, density=True, alpha=0.6, color='g')
    
    # Fit a normal distribution to the data
    fit = norm.pdf(bins, mean, std_dev)
    
    # Plot the PDF of the normal distribution
    ax.plot(bins, fit, 'r-', lw=2)
    
    # Set the title of the plot with the fit results
    ax.set_title(f'Fit results: mean = {mean:.2f}, std = {std_dev:.2f}')
    
    # Return the figure and the samples
    return fig, samples
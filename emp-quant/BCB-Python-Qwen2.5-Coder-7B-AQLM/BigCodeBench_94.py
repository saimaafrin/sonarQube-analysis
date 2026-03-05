
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

def task_func(mean, std_dev, num_samples):
    # Generate samples from a normal distribution
    samples = np.random.normal(mean, std_dev, num_samples)
    
    # Create a histogram of the samples
    fig, ax = plt.subplots()
    ax.hist(samples, bins=30, density=True, alpha=0.6, color='g')
    
    # Plot the probability density function of the normal distribution
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mean, std_dev)
    ax.plot(x, p, 'k', linewidth=2)
    
    # Set the title of the plot with the fit results
    ax.set_title(f'Fit results: mean = {mean:.2f}, std = {std_dev:.2f}')
    
    # Return the figure object and the samples array
    return fig, samples

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

def task_func(mean, std_dev, num_samples):
    # Generate samples from a normal distribution
    samples = np.random.normal(mean, std_dev, num_samples)
    
    # Create a histogram of the samples
    fig, ax = plt.subplots()
    ax.hist(samples, bins=30, density=True, alpha=0.6, color='g')
    
    # Fit a normal distribution to the samples
    fit = norm.pdf(x, mean, std_dev)
    
    # Overlay the PDF of the normal distribution
    ax.plot(x, fit, "r--")
    
    # Set the title with the fit results
    ax.set_title(f"Fit results: mean = {mean:.2f}, std = {std_dev:.2f}")
    
    # Return the figure object and the samples
    return fig, samples
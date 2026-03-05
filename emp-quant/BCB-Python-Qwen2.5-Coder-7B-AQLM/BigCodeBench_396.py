
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def task_func(mu, sigma, sample_size, seed=0):
    # Set the seed for reproducibility
    np.random.seed(seed)
    
    # Generate a random sample from a normal distribution
    sample = np.random.normal(mu, sigma, sample_size)
    
    # Create a range of values for the x-axis
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
    
    # Calculate the density of the normal distribution
    density = stats.norm.pdf(x, mu, sigma)
    
    # Create a plot
    fig, ax = plt.subplots()
    
    # Plot the density
    ax.plot(x, density, label='Normal Distribution')
    
    # Plot the histogram of the sample
    ax.hist(sample, bins=30, density=True, alpha=0.5, label='Sample')
    
    # Add a legend
    ax.legend()
    
    # Return the axes object
    return ax
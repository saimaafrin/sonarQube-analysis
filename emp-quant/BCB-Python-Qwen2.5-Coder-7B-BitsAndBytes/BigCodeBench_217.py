
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def task_func(mu=0, sigma=1, sample_size=1000, seed=0):
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Generate a sample from a normal distribution
    sample = np.random.normal(mu, sigma, sample_size)
    
    # Calculate the empirical mean and standard deviation
    empirical_mean = np.mean(sample)
    empirical_std = np.std(sample)
    
    # Create a figure and axis for plotting
    fig, ax = plt.subplots()
    
    # Plot the histogram of the sample
    n, bins, patches = ax.hist(sample, bins=30, density=True, alpha=0.6, color='g')
    
    # Plot the probability density function of the normal distribution
    x = np.linspace(mu - 4*sigma, mu + 4*sigma, 100)
    y = stats.norm.pdf(x, mu, sigma)
    ax.plot(x, y, 'r-', linewidth=2)
    
    # Set the title of the plot
    ax.set_title(f'Normal Distribution with $\\mu = {mu:.2f}, \\sigma = {sigma:.2f}$')
    
    # Return the axes object, empirical mean, and empirical standard deviation
    return ax, empirical_mean, empirical_std
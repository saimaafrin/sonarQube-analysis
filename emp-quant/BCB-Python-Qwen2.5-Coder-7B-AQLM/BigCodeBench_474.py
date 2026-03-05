
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def task_func(n_samples=1000, mu=0, sigma=1, random_seed=0):
    """
    Generates a histogram and a probability density function (PDF) plot for a specified normal distribution.
    
    Parameters:
    - n_samples (int): Number of samples to draw from the normal distribution.
    - mu (float): Mean of the normal distribution.
    - sigma (float): Standard deviation of the normal distribution.
    - random_seed (int): Seed for the random number generator for reproducibility.
    
    Returns:
    - ax (matplotlib.axes._axes.Axes): Axes object with the histogram and PDF plotted.
    - samples (numpy.ndarray): Generated sample data.
    """
    # Set the random seed for reproducibility
    np.random.seed(random_seed)
    
    # Generate samples from the normal distribution
    samples = np.random.normal(mu, sigma, n_samples)
    
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Plot the histogram of the samples with normalized density
    ax.hist(samples, bins=30, density=True, alpha=0.6, color='g')
    
    # Plot the PDF of the normal distribution
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
    ax.plot(x, norm.pdf(x, mu, sigma), 'r', linewidth=2)
    
    # Set the title and labels
    ax.set_title('Histogram and PDF of Normal Distribution')
    ax.set_xlabel('Value')
    ax.set_ylabel('Probability Density')
    
    # Show the plot
    plt.show()
    
    return ax, samples
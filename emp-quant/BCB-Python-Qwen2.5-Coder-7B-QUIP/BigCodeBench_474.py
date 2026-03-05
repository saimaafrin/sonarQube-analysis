
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def task_func(n_samples=1000, mu=0, sigma=1, random_seed=0):
    """
    Generates a histogram and a probability density function (PDF) plot for a specified normal distribution.
    
    Parameters:
    n_samples (int): Number of samples to generate from the normal distribution.
    mu (float): The mean of the normal distribution.
    sigma (float): The standard deviation of the normal distribution.
    random_seed (int): The seed for the random number generator.
    
    Returns:
    ax (matplotlib.axes._axes.Axes): Axes object with the histogram and PDF plotted.
    samples (numpy.ndarray): Generated sample data.
    """
    # Set the random seed for reproducibility
    np.random.seed(random_seed)
    
    # Generate samples from the normal distribution
    samples = np.random.normal(mu, sigma, n_samples)
    
    # Create the figure and axes
    fig, ax = plt.subplots()
    
    # Plot the histogram of the samples
    ax.hist(samples, bins=30, density=True, alpha=0.6, label='Histogram')
    
    # Plot the PDF of the normal distribution
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
    ax.plot(x, norm.pdf(x, mu, sigma), 'r', linewidth=2, label='PDF')
    
    # Set the labels and title
    ax.set_xlabel('Value')
    ax.set_ylabel('Density')
    ax.set_title('Normal Distribution')
    ax.legend()
    
    # Return the axes object and the samples
    return ax, samples
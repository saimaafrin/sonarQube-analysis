import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
def task_func(mu=0, sigma=1, sample_size=1000, seed=0):
    """
    Generate a sample from a normal distribution with a given mean and standard deviation,
    plot the histogram together with the probability density function, and return the Axes object,
    empirical mean, and empirical standard deviation of the sample.
    
    Parameters:
    - mu (float): The mean of the normal distribution.
    - sigma (float): The standard deviation of the normal distribution.
    - sample_size (int): The number of samples to generate.
    - seed (int): The seed for the random number generator for reproducibility.
    
    Returns:
    - ax (matplotlib.axes._axes.Axes): Axes object with the plotted histogram and normal PDF.
    - float: The empirical mean of the sample.
    - float: The empirical standard deviation of the sample.
    """
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Generate the sample from the normal distribution
    sample = np.random.normal(mu, sigma, sample_size)
    
    # Calculate the empirical mean and standard deviation
    empirical_mean = np.mean(sample)
    empirical_std = np.std(sample)
    
    # Create a figure and axis for plotting
    fig, ax = plt.subplots()
    
    # Plot the histogram of the sample
    ax.hist(sample, bins=30, density=True, alpha=0.6, color='g')
    
    # Plot the probability density function of the normal distribution
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
    ax.plot(x, stats.norm.pdf(x, mu, sigma), 'r-', lw=2)
    
    # Set the title of the plot
    ax.set_title(f'Normal Distribution with $\\mu = {mu:.2f}, \\sigma = {sigma:.2f}$')
    
    # Return the Axes object, empirical mean, and empirical standard deviation
    return ax, empirical_mean, empirical_std
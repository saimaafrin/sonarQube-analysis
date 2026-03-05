
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def task_func(mu=0, sigma=1, sample_size=1000, seed=0):
    """
    Generate a sample from a normal distribution with a given mean and a standard deviation and plot the histogram together with the probability density function.
    
    Parameters:
    mu (float): The mean of the normal distribution.
    sigma (float): The standard deviation of the normal distribution.
    sample_size (int): The number of samples to generate.
    seed (int): The seed for the random number generator.
    
    Returns:
    ax (matplotlib.axes._axes.Axes): Axes object with the plotted histogram and normal PDF.
    float: The empirical mean of the sample.
    float: The empirical standard deviation of the sample.
    """
    # Set the seed for the random number generator
    np.random.seed(seed)
    
    # Generate the sample
    sample = np.random.normal(mu, sigma, sample_size)
    
    # Calculate the empirical mean and standard deviation
    empirical_mean = np.mean(sample)
    empirical_std = np.std(sample)
    
    # Create the plot
    fig, ax = plt.subplots()
    ax.hist(sample, bins=30, density=True, alpha=0.6, color='g')
    xmin, xmax = ax.get_xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, mu, sigma)
    ax.plot(x, p, 'k', linewidth=2)
    ax.set_title(f'Normal Distribution with $\\mu = {mu:.2f}, \\sigma = {sigma:.2f}$')
    
    return ax, empirical_mean, empirical_std
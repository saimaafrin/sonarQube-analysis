import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
def task_func(mu, sigma, seed=0):
    """
    Draws a normal distribution using a 1000 samples, indicating the mean and standard deviation with a color bar.
    
    Parameters:
    - mu: The mean of the normal distribution.
    - sigma: The standard deviation of the normal distribution.
    - seed: The seed for the random number generator for reproducibility.
    
    Returns:
    - matplotlib.axes._axes.Axes: The Axes object of the plotted distribution.
    """
    # Set the seed for reproducibility
    np.random.seed(seed)
    
    # Generate 1000 samples from a normal distribution
    samples = np.random.normal(mu, sigma, 1000)
    
    # Create a histogram of the samples
    ax = sns.histplot(samples, kde=True, color='blue', edgecolor='black')
    
    # Add a vertical line at the mean
    ax.axvline(mu, color='red', linestyle='dashed', linewidth=2)
    
    # Add a vertical line at one standard deviation from the mean
    ax.axvline(mu + sigma, color='green', linestyle='dashed', linewidth=2)
    ax.axvline(mu - sigma, color='green', linestyle='dashed', linewidth=2)
    
    # Add a color bar to indicate the density
    ax.set_title(f'Normal Distribution with Mean={mu} and Std={sigma}')
    ax.set_xlabel('Value')
    ax.set_ylabel('Density')
    
    return ax
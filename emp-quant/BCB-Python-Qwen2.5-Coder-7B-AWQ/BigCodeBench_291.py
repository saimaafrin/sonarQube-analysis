import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
def task_func(mu, sigma, seed=0):
    """
    Draws a normal distribution using a 1000 samples, indicating the mean and standard deviation with a color bar.
    
    Parameters:
    - mu (float): The mean of the normal distribution.
    - sigma (float): The standard deviation of the normal distribution.
    - seed (int): The seed for the random number generator for reproducibility.
    
    Returns:
    - matplotlib.axes._axes.Axes: The Axes object of the plotted distribution.
    """
    # Set the seed for reproducibility
    np.random.seed(seed)
    
    # Generate 1000 samples from a normal distribution
    samples = np.random.normal(mu, sigma, 1000)
    
    # Create a histogram of the samples
    ax = sns.histplot(samples, kde=True, color='blue', stat='density')
    
    # Add a vertical line at the mean
    ax.axvline(mu, color='red', linestyle='--', label='Mean')
    
    # Add a vertical line at the standard deviation boundaries
    ax.axvline(mu - sigma, color='green', linestyle='--', label='Mean - 1 Std')
    ax.axvline(mu + sigma, color='green', linestyle='--', label='Mean + 1 Std')
    
    # Add a color bar indicating the density
    ax.figure.colorbar(ax.lines[0], ax=ax, label='Density')
    
    # Set the title and labels
    ax.set_title('Normal Distribution')
    ax.set_xlabel('Value')
    ax.set_ylabel('Density')
    
    # Show the legend
    ax.legend()
    
    # Return the Axes object
    return ax
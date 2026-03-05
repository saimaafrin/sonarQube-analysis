
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def task_func(mu, sigma, seed=0):
    # Set the seed for reproducibility
    np.random.seed(seed)
    
    # Generate 1000 samples from a normal distribution
    samples = np.random.normal(mu, sigma, 1000)
    
    # Create a histogram of the samples
    ax = sns.histplot(samples, kde=True, color='blue', bins=30)
    
    # Add a vertical line at the mean
    ax.axvline(mu, color='red', linestyle='dashed', linewidth=2)
    
    # Add a vertical line at one standard deviation from the mean
    ax.axvline(mu + sigma, color='green', linestyle='dashed', linewidth=2)
    ax.axvline(mu - sigma, color='green', linestyle='dashed', linewidth=2)
    
    # Add a color bar to indicate the density
    ax.set_title(f'Normal Distribution with Mean={mu} and Std={sigma}')
    ax.set_xlabel('Value')
    ax.set_ylabel('Density')
    
    # Return the Axes object
    return ax
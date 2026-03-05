import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
def task_func(mu, sigma, seed=0):
    """
    Draws a normal distribution using a 1000 samples, indicating the mean and standard deviation with a color bar.
    
    Parameters:
    - mu: Mean of the normal distribution.
    - sigma: Standard deviation of the normal distribution.
    - seed: Seed for the random number generator for reproducibility.
    
    Returns:
    - matplotlib.axes._axes.Axes: The Axes object of the plotted distribution.
    """
    # Set the seed for reproducibility
    np.random.seed(seed)
    
    # Generate 1000 samples from a normal distribution
    samples = np.random.normal(mu, sigma, 1000)
    
    # Create a figure and an axes object
    fig, ax = plt.subplots()
    
    # Plot the histogram of the samples
    sns.histplot(samples, kde=True, color='blue', ax=ax)
    
    # Add a vertical line at the mean
    ax.axvline(mu, color='red', linestyle='--', label=f'Mean: {mu}')
    
    # Add a vertical line at the standard deviation boundaries
    ax.axvline(mu - sigma, color='green', linestyle='--', label=f'Standard Deviation: {sigma}')
    ax.axvline(mu + sigma, color='green', linestyle='--')
    
    # Add a legend
    ax.legend()
    
    # Set the title and labels
    ax.set_title('Normal Distribution')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    
    # Show the plot
    plt.show()
    
    # Return the axes object
    return ax
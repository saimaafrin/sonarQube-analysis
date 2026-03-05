
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def task_func(mu, sigma, seed=0):
    """
    Draws a normal distribution using a 1000 samples, indicating the mean and standard deviation with a color bar.
    
    Parameters:
    mu (float): The mean of the normal distribution.
    sigma (float): The standard deviation of the normal distribution.
    seed (int): The random seed for reproducibility.
    
    Returns:
    matplotlib.axes._axes.Axes: The Axes object of the plotted distribution.
    """
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Generate 1000 samples from a normal distribution
    samples = np.random.normal(mu, sigma, 1000)
    
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Plot the histogram of the samples
    sns.histplot(samples, kde=True, color='blue', ax=ax)
    
    # Add a vertical line at the mean
    ax.axvline(mu, color='red', linestyle='dashed', linewidth=1)
    
    # Add a vertical line at the standard deviation boundaries
    ax.axvline(mu - sigma, color='green', linestyle='dashed', linewidth=1)
    ax.axvline(mu + sigma, color='green', linestyle='dashed', linewidth=1)
    
    # Set the title and labels
    ax.set_title('Normal Distribution')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    
    # Show the plot
    plt.show()
    
    # Return the Axes object
    return ax
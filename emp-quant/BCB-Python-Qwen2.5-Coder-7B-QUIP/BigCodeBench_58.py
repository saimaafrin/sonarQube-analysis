
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def task_func(mu, sigma, num_samples):
    """
    Display a plot showing a normal distribution with a given mean and standard deviation
    and overlay a histogram of randomly generated samples from this distribution.
    
    Parameters:
    mu (float): The mean of the normal distribution.
    sigma (float): The standard deviation of the normal distribution.
    num_samples (int): The number of samples to generate from the normal distribution.
    
    Returns:
    fig (matplotlib.figure.Figure): The generated figure.
    """
    # Generate samples from the normal distribution
    samples = np.random.normal(mu, sigma, num_samples)
    
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Plot the normal distribution
    ax.plot([mu], [0], 'ro', label=f'μ={mu}, σ={sigma}')
    ax.plot([mu - sigma, mu + sigma], [0.5, 0.5], 'r--', label='1σ')
    
    # Overlay the histogram of the samples
    ax.hist(samples, bins=30, density=True, alpha=0.6, color='b')
    
    # Add labels and title
    ax.set_xlabel('Value')
    ax.set_ylabel('Density')
    ax.set_title('Normal Distribution')
    ax.legend()
    
    # Show the plot
    plt.show()
    
    return fig
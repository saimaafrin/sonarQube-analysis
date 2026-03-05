import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
def task_func(mu, sigma, num_samples):
    """
    Generate a plot showing a normal distribution with a given mean and standard deviation
    and overlay a histogram of randomly generated samples from this distribution.

    Parameters:
    mu (float): The mean of the normal distribution.
    sigma (float): The standard deviation of the normal distribution.
    num_samples (int): The number of samples to generate.

    Returns:
    fig (matplotlib.figure.Figure): The generated figure.
    """
    # Generate samples from the normal distribution
    samples = np.random.normal(mu, sigma, num_samples)
    
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Plot the normal distribution curve
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
    ax.plot(x, stats.norm.pdf(x, mu, sigma), 'r-', lw=2, label='Normal distribution')
    
    # Overlay the histogram of the samples
    ax.hist(samples, bins=30, density=True, alpha=0.6, color='g', label='Sample histogram')
    
    # Set the title and labels
    ax.set_title('Normal Distribution')
    ax.set_xlabel('Value')
    ax.set_ylabel('Probability')
    
    # Add a legend
    ax.legend()
    
    return fig
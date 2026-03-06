
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def task_func(mu, sigma, num_samples):
    """
    Generates a plot showing a normal distribution with a given mean and standard deviation 
    and overlays a histogram of randomly generated samples from this distribution.

    Parameters:
    mu (float): The mean of the normal distribution.
    sigma (float): The standard deviation of the normal distribution.
    num_samples (int): The number of samples to generate for the histogram.

    Returns:
    fig (matplotlib.figure.Figure): The generated figure.
    """

    # Generate random samples from the normal distribution
    samples = np.random.normal(mu, sigma, num_samples)

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Plot the normal distribution curve
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
    y = stats.norm.pdf(x, mu, sigma)
    ax.plot(x, y, label='Normal Distribution')

    # Overlay the histogram of the samples
    ax.hist(samples, bins=30, density=True, alpha=0.6, color='g', label='Histogram')

    # Set the title and labels
    ax.set_title('Normal Distribution')
    ax.set_xlabel('Value')
    ax.set_ylabel('Density')

    # Add legend
    ax.legend()

    return fig
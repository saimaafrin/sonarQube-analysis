
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def task_func(n_samples=1000, mu=0, sigma=1, random_seed=0):
    """
    Generates a histogram and a probability density function (PDF) plot for a specified normal distribution.

    Parameters:
    - n_samples: int, number of samples to generate.
    - mu: float, mean of the normal distribution.
    - sigma: float, standard deviation of the normal distribution.
    - random_seed: int, seed for the random number generator for reproducibility.

    Returns:
    - ax: matplotlib.axes._axes.Axes, Axes object with the histogram and PDF plotted.
    - samples: numpy.ndarray, generated sample data.
    """
    # Set the random seed for reproducibility
    np.random.seed(random_seed)
    
    # Generate samples from the normal distribution
    samples = np.random.normal(mu, sigma, n_samples)
    
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Plot the histogram of the samples with normalized density
    counts, bins, ignored = ax.hist(samples, bins=30, density=True, alpha=0.6, color='g')
    
    # Calculate the bin centers
    bin_centers = (bins[:-1] + bins[1:]) / 2
    
    # Plot the PDF of the normal distribution
    pdf_values = norm.pdf(bin_centers, mu, sigma)
    ax.plot(bin_centers, pdf_values, 'r-', linewidth=2)
    
    # Set labels and title
    ax.set_xlabel('Value')
    ax.set_ylabel('Probability Density')
    ax.set_title(f'Normal Distribution (μ={mu}, σ={sigma})')
    
    return ax, samples
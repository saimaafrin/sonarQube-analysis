
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def task_func(mu, sigma, num_samples=1000, seed=77):
    """
    Generates a normal distribution with the given mean and standard deviation.
    Creates a figure containing a histogram and a Q-Q plot of the generated samples.

    Parameters:
    mu (float): The mean of the normal distribution.
    sigma (float): The standard deviation of the normal distribution.
    num_samples (int): The number of samples to generate.
    seed (int): The seed for the random number generator.

    Returns:
    matplotlib.figure.Figure: A matplotlib figure containing the histogram and Q-Q plot.
    """
    # Set the seed for the random number generator
    np.random.seed(seed)

    # Generate the samples from the normal distribution
    samples = np.random.normal(mu, sigma, num_samples)

    # Create a figure with a 1x2 grid of subplots
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))

    # Plot the histogram of the samples
    axs[0].hist(samples, bins=30, density=True, color='k', alpha=0.7)
    axs[0].set_title(f'Normal Distribution (μ={mu}, σ={sigma})')
    axs[0].set_xlabel('Value')
    axs[0].set_ylabel('Density')

    # Create a Q-Q plot
    stats.probplot(samples, dist='norm', plot=axs[1], fit=True, color='k')

    # Return the figure
    return fig
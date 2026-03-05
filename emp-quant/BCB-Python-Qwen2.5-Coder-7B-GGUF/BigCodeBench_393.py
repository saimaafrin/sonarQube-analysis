
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
    # Set the seed for reproducibility
    np.random.seed(seed)
    
    # Generate the normal distribution samples
    samples = np.random.normal(mu, sigma, num_samples)
    
    # Create a figure with two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Plot the histogram
    ax1.hist(samples, bins=30, density=True, alpha=0.6, color='g')
    ax1.set_title('Histogram of the Generated Samples')
    ax1.set_xlabel('Value')
    ax1.set_ylabel('Density')
    
    # Plot the Q-Q plot
    stats.probplot(samples, dist="norm", plot=ax2)
    ax2.set_title('Q-Q Plot of the Generated Samples')
    
    return fig
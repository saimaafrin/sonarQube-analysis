
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def task_func(mu, sigma, num_samples):
    # Generate random samples from the normal distribution
    samples = stats.norm.rvs(mu, sigma, size=num_samples)

    # Create the figure and axis objects
    fig, ax = plt.subplots()

    # Plot the normal distribution
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
    ax.plot(x, stats.norm.pdf(x, mu, sigma), label='Normal distribution')

    # Overlay the histogram of the random samples
    ax.hist(samples, bins=50, alpha=0.5, label='Samples')

    # Set the plot title and labels
    ax.set_title('Normal Distribution')
    ax.set_xlabel('Value')
    ax.set_ylabel('Density')
    ax.legend()

    # Return the figure object
    return fig

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def task_func(mu, sigma, num_samples):
    # Generate random samples from the normal distribution
    samples = stats.norm.rvs(mu, sigma, size=num_samples)

    # Create the figure and axis objects
    fig, ax = plt.subplots()

    # Plot the normal distribution
    ax.plot(stats.norm.pdf(np.linspace(-3, 3, 100), mu, sigma), label='Normal Distribution')

    # Plot the histogram of the samples
    ax.hist(samples, bins=20, density=True, alpha=0.5, label='Samples')

    # Set the plot title and labels
    ax.set_title('Normal Distribution')
    ax.set_xlabel('Value')
    ax.set_ylabel('Probability')
    ax.legend()

    # Return the figure
    return fig

# Show the figures
plt.show()
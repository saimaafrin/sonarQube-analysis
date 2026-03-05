
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def task_func(n_samples=1000, mu=0, sigma=1, random_seed=0):
    # Generate samples from a normal distribution
    samples = np.random.normal(mu, sigma, n_samples)

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Plot the histogram of the samples
    ax.hist(samples, bins=50, normed=True)

    # Plot the PDF of the normal distribution
    x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)
    ax.plot(x, norm.pdf(x, mu, sigma), 'r', linewidth=2)

    # Set the axis labels
    ax.set_xlabel('Value')
    ax.set_ylabel('Density')

    # Return the axes object
    return ax
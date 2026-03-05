
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def task_func(n_samples=1000, mu=0, sigma=1, random_seed=0):
    # Set random seed for reproducibility
    np.random.seed(random_seed)

    # Generate samples from normal distribution
    samples = np.random.normal(mu, sigma, n_samples)

    # Create histogram of samples
    ax = plt.hist(samples, bins=50, density=True, alpha=0.5, label='Histogram')

    # Overlay PDF of normal distribution
    x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 1000)
    y = norm.pdf(x, mu, sigma)
    ax.plot(x, y, color='red', linewidth=2, label='PDF')

    # Set axis labels and legend
    ax.set_xlabel('Value')
    ax.set_ylabel('Density')
    ax.legend()

    return ax, samples
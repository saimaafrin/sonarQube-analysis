
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def task_func(n_samples=1000, mu=0, sigma=1, random_seed=0):
    # Generate n_samples from a normal distribution
    np.random.seed(random_seed)
    samples = np.random.normal(mu, sigma, n_samples)

    # Plot the histogram and PDF
    fig, ax = plt.subplots()
    ax.hist(samples, density=True, bins=50, alpha=0.5, label='Histogram')
    ax.plot(samples, norm.pdf(samples, mu, sigma), color='red', linewidth=2, label='PDF')
    ax.set_xlabel('Value')
    ax.set_ylabel('Density')
    ax.legend()
    plt.show()

    return ax, samples
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
def task_func(n_samples=1000, mu=0, sigma=1, random_seed=0):
    np.random.seed(random_seed)
    samples = np.random.normal(mu, sigma, n_samples)
    ax = plt.hist(samples, bins=50, density=True, alpha=0.5, label='Histogram')
    ax.plot(norm.pdf(samples, mu, sigma), color='red', linewidth=2, label='PDF')
    ax.set_xlabel('Value')
    ax.set_ylabel('Density')
    ax.legend()
    return ax, samples
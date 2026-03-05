
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def task_func(mu, sigma, num_samples=1000, seed=77):
    np.random.seed(seed)
    samples = np.random.normal(mu, sigma, num_samples)
    fig, axs = plt.subplots(2, 1, figsize=(10, 6))
    axs[0].hist(samples, bins=50, density=True, alpha=0.5, label='Histogram')
    axs[0].set_xlabel('Value')
    axs[0].set_ylabel('Density')
    axs[0].legend()
    axs[1].plot(stats.norm.ppf(stats.norm.cdf(samples)), 'o-', label='Q-Q Plot')
    axs[1].set_xlabel('Theoretical Quantiles')
    axs[1].set_ylabel('Sample Quantiles')
    axs[1].legend()
    fig.tight_layout()
    return fig
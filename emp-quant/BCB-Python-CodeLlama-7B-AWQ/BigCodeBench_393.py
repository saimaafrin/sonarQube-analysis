import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
def task_func(mu, sigma, num_samples=1000, seed=77):
    """
    Generate a normal distribution with the given mean and standard deviation.
    Creates a figure containing a histogram and a Q-Q plot of the generated samples.
    """
    np.random.seed(seed)
    samples = np.random.normal(mu, sigma, num_samples)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    ax1.hist(samples, bins=50, density=True, alpha=0.5, label='Histogram')
    ax1.set_xlabel('Value')
    ax1.set_ylabel('Density')
    ax1.legend()
    ax2.plot(stats.norm.ppf(stats.norm.cdf(samples)), label='Q-Q plot')
    ax2.set_xlabel('Theoretical quantiles')
    ax2.set_ylabel('Empirical quantiles')
    ax2.legend()
    return fig
mu = 0
sigma = 1
num_samples = 1000
seed = 77
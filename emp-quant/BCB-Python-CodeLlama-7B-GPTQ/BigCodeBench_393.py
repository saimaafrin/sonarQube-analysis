import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
def task_func(mu, sigma, num_samples=1000, seed=77):
    """
    Generate a normal distribution with the given mean and standard deviation.
    Creates a figure containing a histogram and a Q-Q plot of the generated samples.

    Args:
        mu (float): mean of the normal distribution
        sigma (float): standard deviation of the normal distribution
        num_samples (int, optional): number of samples to generate. Defaults to 1000.
        seed (int, optional): random seed. Defaults to 77.

    Returns:
        matplotlib.figure.Figure: A matplotlib figure containing the histogram and Q-Q plot.
    """
    np.random.seed(seed)
    samples = np.random.normal(mu, sigma, num_samples)
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].hist(samples, bins=50, alpha=0.5, label=f"Histogram of {num_samples} samples")
    axs[0].set_title(f"Histogram of {num_samples} samples")
    axs[1].plot(stats.norm.ppf(stats.norm.cdf(samples)), label=f"Q-Q plot of {num_samples} samples")
    axs[1].set_title(f"Q-Q plot of {num_samples} samples")
    axs[1].set_xlabel("Theoretical quantiles")
    axs[1].set_ylabel("Sample quantiles")
    axs[1].legend()
    return fig
mu = 0
sigma = 1
num_samples = 1000
seed = 77
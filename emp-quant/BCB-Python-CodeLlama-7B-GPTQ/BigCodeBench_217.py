import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
def task_func(mu=0, sigma=1, sample_size=1000, seed=0):
    np.random.seed(seed)
    sample = np.random.normal(mu, sigma, sample_size)
    ax = plt.hist(sample, bins=50, density=True, alpha=0.5, label='Sample')
    ax.set_title(f'Normal Distribution with $\\mu = {mu}, \\sigma = {sigma}$')
    ax.set_xlabel('Value')
    ax.set_ylabel('Probability Density')
    ax.legend()
    empirical_mean = np.mean(sample)
    empirical_std = np.std(sample)
    return ax, empirical_mean, empirical_std
mu = 0
sigma = 1
sample_size = 1000
seed = 0
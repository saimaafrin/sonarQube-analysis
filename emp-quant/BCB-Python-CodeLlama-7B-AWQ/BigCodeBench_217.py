import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
def task_func(mu=0, sigma=1, sample_size=1000, seed=0):
    np.random.seed(seed)
    sample = np.random.normal(mu, sigma, sample_size)
    ax = plt.hist(sample, bins=50, density=True, alpha=0.5, label='Sample')
    ax.set_title(f'Normal Distribution with $\\mu = {mu}, \\sigma = {sigma}$')
    ax.set_xlabel('Value')
    ax.set_ylabel('Density')
    ax.legend()
    ax.set_xlim([-3, 3])
    ax.set_ylim([0, 0.2])
    return ax, np.mean(sample), np.std(sample)
mu = 0
sigma = 1
sample_size = 1000
seed = 0
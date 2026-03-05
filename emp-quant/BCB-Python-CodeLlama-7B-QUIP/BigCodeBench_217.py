
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def task_func(mu=0, sigma=1, sample_size=1000, seed=0):
    np.random.seed(seed)
    sample = stats.norm.rvs(mu, sigma, sample_size)
    ax = plt.hist(sample, bins=50, label='Sample')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title('Normal Distribution with $\mu = %0.2f, \\sigma = %0.2f$' % (mu, sigma))
    ax.hist(stats.norm.pdf(sample, mu, sigma), bins=50, label='PDF')
    ax.legend()
    return ax, np.mean(sample), np.std(sample)

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def task_func(mu, sigma, sample_size, seed=0):
    # Generate a random sample from a normal distribution
    np.random.seed(seed)
    x = np.random.normal(mu, sigma, sample_size)

    # Compute the kernel density estimate
    kde = stats.gaussian_kde(x)

    # Plot the density estimate
    fig, ax = plt.subplots()
    ax.plot(x, kde(x))
    ax.set_xlabel('Value')
    ax.set_ylabel('Density')
    ax.set_title('Gaussian Kernel Density Estimate')

    return ax
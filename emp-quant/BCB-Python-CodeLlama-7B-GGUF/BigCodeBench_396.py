
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def task_func(mu, sigma, sample_size, seed=0):
    np.random.seed(seed)
    x = np.random.normal(mu, sigma, size=sample_size)
    y = stats.norm.pdf(x, mu, sigma)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.set_title('Gaussian Kernel Density Estimate')
    return ax
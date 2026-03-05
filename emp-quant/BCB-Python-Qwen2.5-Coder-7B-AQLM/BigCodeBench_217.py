
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def task_func(mu=0, sigma=1, sample_size=1000, seed=0):
    np.random.seed(seed)
    sample = np.random.normal(mu, sigma, sample_size)
    
    # Calculate empirical mean and standard deviation
    empirical_mean = np.mean(sample)
    empirical_std = np.std(sample)
    
    # Plot the histogram and normal PDF
    fig, ax = plt.subplots()
    ax.hist(sample, bins=30, density=True, alpha=0.6, color='g')
    
    # Plot the normal PDF
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, mu, sigma)
    ax.plot(x, p, 'k', linewidth=2)
    
    # Set the title of the plot
    ax.set_title(f'Normal Distribution with $\\mu = {mu:.2f}, \\sigma = {sigma:.2f}$')
    
    return ax, empirical_mean, empirical_std
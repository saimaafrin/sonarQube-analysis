
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def task_func(mean, std_dev, n):
    # Generate samples from a normal distribution
    samples = np.random.normal(mean, std_dev, n)
    
    # Plot the histogram of the generated samples
    plt.hist(samples, bins=30, density=True, alpha=0.6, color='g')
    
    # Plot the probability density function
    x = np.linspace(mean - 3*std_dev, mean + 3*std_dev, 100)
    plt.plot(x, stats.norm.pdf(x, mean, std_dev), 'r-', lw=2)
    
    # Show the plot
    plt.show()
    
    return samples
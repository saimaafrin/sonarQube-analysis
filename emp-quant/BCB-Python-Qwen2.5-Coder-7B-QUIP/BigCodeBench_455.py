
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def task_func(mean, std_dev, n):
    # Generate samples from a normal distribution
    samples = np.random.normal(mean, std_dev, n)
    
    # Plot the histogram of the generated samples
    plt.hist(samples, bins=30, density=True, alpha=0.6, color='g')
    
    # Plot the probability density function of the normal distribution
    x = np.linspace(mean - 3*std_dev, mean + 3*std_dev, 100)
    plt.plot(x, stats.norm.pdf(x, mean, std_dev), 'r')
    plt.title(f'Normal Distribution with mean {mean} and std_dev {std_dev}')
    plt.xlabel('Value')
    plt.ylabel('Density')
    plt.show()
    
    return samples
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
def task_func(mean, std_dev, n):
    """
    Generates a set of samples from a normal distribution with a specified mean and standard deviation.
    
    Parameters:
    - mean (float): The mean of the normal distribution.
    - std_dev (float): The standard deviation of the normal distribution.
    - n (int): The number of samples to generate.
    
    Returns:
    - numpy.ndarray: An array of generated samples from the normal distribution.
    """
    # Generate samples from a normal distribution
    samples = np.random.normal(mean, std_dev, n)
    
    # Plot the histogram of the generated samples
    plt.hist(samples, bins=30, density=True, alpha=0.6, color='g')
    
    # Plot the probability density function of the normal distribution
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, mean, std_dev)
    plt.plot(x, p, 'k', linewidth=2)
    
    # Show the plot
    plt.show()
    
    return samples
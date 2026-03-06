
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def task_func(mean, std_dev, n):
    # Generate samples from a normal distribution
    samples = np.random.normal(mean, std_dev, n)
    
    # Plotting the histogram of the generated samples
    plt.hist(samples, bins=30, density=True, alpha=0.6, color='g')
    
    # Plotting the probability density function
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, mean, std_dev)
    plt.plot(x, p, 'k', linewidth=2)
    title = "Fit results: mu = %.2f,  std = %.2f" % (mean, std_dev)
    plt.title(title)
    plt.show()
    
    return samples
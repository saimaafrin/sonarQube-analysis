
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

def task_func(length):
    # Generate a normal distribution with mean 0 and standard deviation 1
    dist = norm.rvs(size=length)

    # Plot the histogram of the distribution
    plt.hist(dist, bins=50, alpha=0.5, label='Histogram')

    # Plot the probability density function of the distribution
    x = np.linspace(-3, 3, 1000)
    plt.plot(x, norm.pdf(x), label='Probability Density Function')

    # Add axis labels and title
    plt.xlabel('Value')
    plt.ylabel('Probability')
    plt.title('Normal Distribution')

    # Add legend and show the plot
    plt.legend()
    plt.show()

    # Return the distribution and the plot
    return dist, plt
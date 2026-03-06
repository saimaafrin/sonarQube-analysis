
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

def task_func(length):
    # Generate a normal distribution with mean 0 and standard deviation 1
    x = np.linspace(-3, 3, length)
    y = norm.pdf(x)

    # Create a histogram of the distribution
    plt.hist(x, bins=50, density=True, alpha=0.5, label='Histogram')

    # Plot the probability density function
    plt.plot(x, y, label='Probability Density Function')

    # Add a title and labels to the plot
    plt.title('Normal Distribution')
    plt.xlabel('Value')
    plt.ylabel('Probability')
    plt.legend()

    # Return the distribution and the plot
    return x, plt.gca()
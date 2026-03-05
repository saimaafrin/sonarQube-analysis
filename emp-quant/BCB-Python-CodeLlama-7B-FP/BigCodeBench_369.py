import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
def task_func(l):
    """
    Draw a histogram of the given array with a Gaussian fit.
    """
    # Calculate the mean and standard deviation of the data
    mean = np.mean(l)
    std = np.std(l)

    # Create a histogram of the data
    n, bins, patches = plt.hist(l, 50, density=True, facecolor='g', alpha=0.75)

    # Add a 'best fit' line
    y = stats.norm.pdf(bins, mean, std)
    plt.plot(bins, y, 'r--')

    # Set the title of the plot
    plt.title(f'Fit results: mu = {mean:.2f},  std = {std:.2f}')

    # Set the x-axis label
    plt.xlabel('Value')

    # Set the y-axis label
    plt.ylabel('Probability')

    # Set the plot size
    plt.rcParams['figure.figsize'] = (10, 6)

    # Return the Axes object with the plot
    return plt.gca()
l = np.random.normal(0, 1, 100)
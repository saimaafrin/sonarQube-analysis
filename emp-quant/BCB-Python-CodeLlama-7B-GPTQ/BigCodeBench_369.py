import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
def task_func(l):
    """
    Draw a histogram of the given array with a Gaussian fit.
    """
    # Calculate the mean and standard deviation of the data
    mu, std = stats.norm.fit(l)

    # Round the mean and standard deviation to two decimal points
    mu = round(mu, 2)
    std = round(std, 2)

    # Create a histogram of the data
    ax = plt.hist(l, bins=20, density=True, alpha=0.5, label='Data')

    # Add a Gaussian fit to the histogram
    x = np.linspace(min(l), max(l), 100)
    y = stats.norm.pdf(x, mu, std)
    ax.plot(x, y, label='Gaussian fit')

    # Set the title of the plot
    ax.set_title(f'Fit results: mu = {mu}, std = {std}')

    # Add a legend to the plot
    ax.legend()

    return ax
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
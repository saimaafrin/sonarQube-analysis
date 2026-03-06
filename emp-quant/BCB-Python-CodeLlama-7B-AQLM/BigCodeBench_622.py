import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from itertools import chain
def task_func(L):
    '''
    Convert a list of lists 'L' into a flattened list of integers, then fit a normal distribution to the data 
    and plot a histogram with the fitted normal distribution overlay.

    Requirements:
    - numpy
    - itertools.chain
    - scipy.stats.norm
    - matplotlib.pyplot

    Parameters:
    L (list of lists): A nested list where each inner list contains integers.

    Returns:
    matplotlib.axes._axes.Axes: Axes object with the plotted histogram and normal distribution overlay.

    Example:
    >>> ax = task_func([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    '''
    # Flatten the list of lists
    L = list(chain.from_iterable(L))

    # Fit a normal distribution to the data
    mu, sigma = norm.fit(L)

    # Plot the histogram
    ax = plt.hist(L, bins=10, density=True)

    # Plot the normal distribution
    x = np.linspace(min(L), max(L), 100)
    y = norm.pdf(x, mu, sigma)
    ax.plot(x, y, 'r--')

    return ax
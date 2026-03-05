import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from itertools import chain
def task_func(L):
    """
    Convert a list of lists 'L' into a flattened list of integers, then fit a normal distribution to the data and plot a histogram with the fitted normal distribution overlay.
    """
    # Flatten the list of lists
    flattened_list = list(chain.from_iterable(L))

    # Fit a normal distribution to the data
    mean, std = norm.fit(flattened_list)

    # Plot the histogram with the fitted normal distribution overlay
    plt.hist(flattened_list, bins='auto', density=True, alpha=0.5, label='Data')
    plt.plot(flattened_list, norm.pdf(flattened_list, mean, std), label='Normal distribution')
    plt.legend()
    plt.show()

    return plt.gca()
L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from itertools import chain
def task_func(L):
    # Flatten the list of lists
    flattened_list = list(chain.from_iterable(L))

    # Fit a normal distribution to the data
    mean, std = norm.fit(flattened_list)

    # Plot the histogram with the fitted normal distribution overlay
    n, bins, patches = plt.hist(flattened_list, bins=50, normed=1, facecolor='green', alpha=0.5)
    plt.plot(bins, norm.pdf(bins, mean, std), 'r--')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram with Normal Distribution Overlay')
    plt.show()

    return plt.gca()
L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
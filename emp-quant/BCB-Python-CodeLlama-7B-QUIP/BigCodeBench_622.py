
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from itertools import chain

def task_func(L):
    # Flatten the list of lists
    flattened_list = list(chain.from_iterable(L))

    # Fit a normal distribution to the data
    mean, std = norm.fit(flattened_list)

    # Plot the histogram with the normal distribution overlay
    n, bins, patches = plt.hist(flattened_list, 50, normed=1, facecolor='green', alpha=0.75, label='Histogram')
    plt.plot(bins, norm.pdf(bins, mean, std), 'r', label='Normal Distribution')
    plt.legend(loc='best')
    plt.show()

    return plt.axes.Axes(n)
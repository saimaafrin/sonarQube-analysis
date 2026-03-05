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
    plt.hist(flattened_list, bins=20, alpha=0.5, label='Data')
    plt.plot(np.linspace(mean - 3 * std, mean + 3 * std, 100),
             norm.pdf(np.linspace(mean - 3 * std, mean + 3 * std, 100),
                      mean, std),
             label='Fitted normal distribution')
    plt.legend()
    plt.show()
L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
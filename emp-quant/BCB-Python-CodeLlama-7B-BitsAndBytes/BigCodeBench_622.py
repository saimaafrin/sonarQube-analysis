
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from itertools import chain

def task_func(L):
    # Flatten the list of lists
    flat_list = list(chain.from_iterable(L))

    # Fit a normal distribution to the data
    mean, std = norm.fit(flat_list)

    # Plot the histogram with the fitted normal distribution overlay
    plt.hist(flat_list, bins=20, density=True, alpha=0.5, label='Data')
    x = np.linspace(min(flat_list), max(flat_list), 100)
    plt.plot(x, norm.pdf(x, mean, std), label='Normal distribution')
    plt.legend()
    plt.show()
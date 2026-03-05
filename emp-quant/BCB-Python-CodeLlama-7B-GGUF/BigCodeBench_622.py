
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
    n, bins, patches = plt.hist(flat_list, bins=50, normed=1, alpha=0.5, label='Data')
    plt.plot(bins, norm.pdf(bins, mean, std), label='Normal distribution')
    plt.legend()
    plt.show()
    
    return plt
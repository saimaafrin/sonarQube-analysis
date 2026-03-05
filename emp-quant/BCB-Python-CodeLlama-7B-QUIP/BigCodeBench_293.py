
import itertools
import numpy as np
import matplotlib.pyplot as plt

def task_func(elements, subset_size):
    subsets = itertools.combinations(elements, subset_size)
    sums = [sum(subset) for subset in subsets]
    histogram = plt.hist(sums, bins=np.arange(0, 100, 1))
    plt.show()
    return histogram, subsets, sums
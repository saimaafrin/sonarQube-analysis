import itertools
import numpy as np
import matplotlib.pyplot as plt
def task_func(elements, subset_size):
    """
    Generate all subsets of a given size from a tuple and draw a histogram of the sums of the subsets.
    Additionally, return the Axes object of the plotted histogram and the combinations of the subsets and their sums.
    """
    # Generate all subsets of the given size from the tuple
    subsets = list(itertools.combinations(elements, subset_size))

    # Calculate the sums of the subsets
    sums = [sum(subset) for subset in subsets]

    # Create a histogram of the sums
    ax = plt.hist(sums, bins=np.arange(min(sums), max(sums) + 1))

    # Return the Axes object of the plotted histogram and the combinations of the subsets and their sums
    return ax, subsets, sums
elements = (1, 2, 3, 4, 5)
subset_size = 3
subsets = list(itertools.combinations(elements, subset_size))
sums = [sum(subset) for subset in subsets]
ax = plt.hist(sums, bins=np.arange(min(sums), max(sums) + 1))
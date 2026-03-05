
import itertools
import numpy as np
import matplotlib.pyplot as plt

def task_func(elements, subset_size):
    # Generate all subsets of the given size
    subsets = list(itertools.combinations(elements, subset_size))
    
    # Calculate the sums of the subsets
    subset_sums = [np.sum(subset) for subset in subsets]
    
    # Plot the histogram of the subset sums
    plt.hist(subset_sums, bins='auto')
    plt.xlabel('Subset Sum')
    plt.ylabel('Frequency')
    plt.title('Histogram of Subset Sums')
    plt.show()
    
    # Return the Axes object of the plotted histogram
    axes = plt.gca()
    
    # Return the combinations of the subsets and their sums
    return axes, subsets, subset_sums
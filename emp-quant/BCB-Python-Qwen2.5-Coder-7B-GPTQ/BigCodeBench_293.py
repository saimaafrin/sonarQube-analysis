import itertools
import numpy as np
import matplotlib.pyplot as plt
def task_func(elements, subset_size):
    # Generate all subsets of the given size
    subsets = list(itertools.combinations(elements, subset_size))
    
    # Calculate the sum of each subset
    subset_sums = [sum(subset) for subset in subsets]
    
    # Plot a histogram of the subset sums
    fig, ax = plt.subplots()
    ax.hist(subset_sums, bins='auto', color='blue', edgecolor='black')
    ax.set_title('Histogram of Subset Sums')
    ax.set_xlabel('Sum')
    ax.set_ylabel('Frequency')
    
    return ax, subsets, subset_sums
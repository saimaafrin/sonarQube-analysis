import itertools
import numpy as np
import matplotlib.pyplot as plt
def task_func(elements, subset_size):
    # Generate all subsets of the given size
    subsets = list(itertools.combinations(elements, subset_size))
    
    # Calculate the sums of each subset
    subset_sums = [sum(subset) for subset in subsets]
    
    # Create a histogram of the subset sums
    plt.hist(subset_sums, bins='auto', alpha=0.7, color='blue')
    plt.title('Histogram of Subset Sums')
    plt.xlabel('Sum')
    plt.ylabel('Frequency')
    plt.grid(True)
    
    # Show the plot
    plt.show()
    
    # Return the Axes object of the plotted histogram and the combinations of subsets and their sums
    return plt.gca(), subsets, subset_sums
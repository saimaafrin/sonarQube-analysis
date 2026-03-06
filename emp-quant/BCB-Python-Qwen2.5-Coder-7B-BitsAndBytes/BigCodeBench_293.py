
import itertools
import numpy as np
import matplotlib.pyplot as plt

def task_func(elements, subset_size):
    # Generate all possible subsets of the given size
    subsets = list(itertools.combinations(elements, subset_size))
    
    # Calculate the sum of each subset
    subset_sums = [sum(subset) for subset in subsets]
    
    # Create a histogram of the subset sums
    fig, ax = plt.subplots()
    ax.hist(subset_sums, bins='auto', color='blue', edgecolor='black')
    ax.set_title(f'Histogram of Subset Sums (Size {subset_size})')
    ax.set_xlabel('Sum of Subsets')
    ax.set_ylabel('Frequency')
    
    return ax, subsets, subset_sums

# Show the plot
plt.show()

# Print the results
print("Subsets:", subsets)
print("Subset Sums:", subset_sums)

import itertools
import numpy as np
import matplotlib.pyplot as plt

def task_func(elements, subset_size):
    # Generate all subsets of the given size from the tuple
    subsets = list(itertools.combinations(elements, subset_size))

    # Calculate the sums of the subsets
    sums = [sum(subset) for subset in subsets]

    # Create a histogram of the sums
    n_bins = 10
    hist, bin_edges = np.histogram(sums, bins=n_bins)

    # Create a bar plot of the histogram
    fig, ax = plt.subplots()
    ax.bar(bin_edges[:-1], hist, width=np.diff(bin_edges))
    ax.set_xlabel('Sum of Subset')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram of Subset Sums')

    # Return the Axes object and the combinations and sums
    return ax, subsets, sums

# Print the combinations and sums
print(subsets)
print(sums)

# Plot the histogram
ax.figure.show()
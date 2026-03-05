import itertools
import numpy as np
import matplotlib.pyplot as plt
def task_func(elements, subset_size):
    """
    Generate all subsets of a given size from a tuple and draw a histogram of the sums of the subsets.
    Additionally, return the Axes object of the plotted histogram and the combinations of the subsets and their sums.
    """
    # Generate all subsets of a given size from a tuple
    subsets = list(itertools.combinations(elements, subset_size))

    # Calculate the sums of the subsets
    sums = [sum(subset) for subset in subsets]

    # Create a histogram of the sums
    n_bins = 100
    hist, bin_edges = np.histogram(sums, bins=n_bins)

    # Plot the histogram
    fig, ax = plt.subplots()
    ax.bar(bin_edges[:-1], hist, width=np.diff(bin_edges))
    ax.set_xlabel('Sum of subset')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram of subset sums')

    # Return the Axes object of the plotted histogram and the combinations of the subsets and their sums
    return ax, subsets, sums
elements = (1, 2, 3, 4, 5)
subset_size = 3

import itertools
import collections

def task_func(elements, subset_size):
    # Generate all subsets of size 2 from the given tuple
    subsets = itertools.combinations(elements, subset_size)

    # Count the occurrences of each sum in the subsets
    sum_counts = collections.Counter(sum(subset) for subset in subsets)

    # Return the dictionary with the sums and their counts
    return sum_counts
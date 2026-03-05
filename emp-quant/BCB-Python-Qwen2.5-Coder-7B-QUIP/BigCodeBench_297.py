
import itertools
import collections

def task_func(elements, subset_size):
    # Generate all possible subsets of the given size
    subsets = list(itertools.combinations(elements, subset_size))
    # Calculate the sum for each subset
    subset_sums = [sum(subset) for subset in subsets]
    # Count occurrences of each sum
    sum_counts = collections.Counter(subset_sums)
    # Return the result as a dictionary
    return dict(sum_counts)
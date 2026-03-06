
import itertools
import collections

def task_func(elements, subset_size):
    # Generate all possible subsets of the given size
    subsets = list(itertools.combinations(elements, subset_size))
    
    # Calculate the sum for each subset and count occurrences
    sum_counts = collections.Counter(sum(subset) for subset in subsets)
    
    return sum_counts
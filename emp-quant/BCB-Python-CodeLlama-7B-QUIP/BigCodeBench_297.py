
import itertools
import collections

def task_func(elements, subset_size):
    subsets = itertools.combinations(elements, subset_size)
    sums = [sum(subset) for subset in subsets]
    counts = collections.Counter(sums)
    return counts
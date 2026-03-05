import itertools
import collections
def task_func(elements, subset_size):
    """
    Generate all 2-element subsets of a tuple and count the occurrences of each sum in the subsets.
    :param elements: A tuple of integers
    :param subset_size: An integer representing the size of the subsets
    :return: A dictionary with the sums and their counts
    """
    # Generate all subsets of the given size
    subsets = itertools.combinations(elements, subset_size)

    # Count the occurrences of each sum in the subsets
    sum_counts = collections.Counter()
    for subset in subsets:
        sum_counts[sum(subset)] += 1

    return sum_counts
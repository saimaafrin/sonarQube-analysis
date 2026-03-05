import itertools
import collections
def task_func(elements, subset_size):
    """
    Generate all 2-element subsets of a tuple and count the occurrences of each sum in the subsets.
    :param elements: A tuple of integers
    :param subset_size: An integer representing the size of the subsets
    :return: A dictionary with the sums and their counts
    """
    # Generate all possible subsets of size 2
    subsets = itertools.combinations(elements, subset_size)

    # Create a dictionary to store the sums and their counts
    sum_counts = collections.defaultdict(int)

    # Iterate over the subsets and count the sums
    for subset in subsets:
        sum_counts[sum(subset)] += 1

    return sum_counts
elements = (1, 2, 3, 4, 5)
subset_size = 2
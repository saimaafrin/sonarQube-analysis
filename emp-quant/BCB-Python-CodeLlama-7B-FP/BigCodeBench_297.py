import itertools
import collections
def task_func(elements, subset_size):
    """
    Generate all 2-element subsets of a tuple and count the occurrences of each sum in the subsets.
    :param elements: The tuple to generate subsets from.
    :param subset_size: The size of the subsets to generate.
    :return: A dictionary with the sums and their counts.
    """
    # Generate all possible subsets of the given size
    subsets = itertools.combinations(elements, subset_size)

    # Initialize a dictionary to store the counts
    counts = collections.Counter()

    # Iterate over the subsets and count the sums
    for subset in subsets:
        sum = sum(subset)
        counts[sum] += 1

    return counts
elements = (1, 2, 3, 4, 5)
subset_size = 2
subsets = itertools.combinations(elements, subset_size)
counts = collections.Counter()
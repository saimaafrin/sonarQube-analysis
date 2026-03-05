import itertools
import math
from pandas import Series
def task_func(elements, subset_size, top_n=2):
    """
    Generate all subsets of a given size from a tuple and calculate the product of the sums of the subsets.
    Additionally, return the top_n sums of the subsets.
    If the subset size is larger than the tuple length, return 1.
    If the subset size is 0, return 1.
    """
    if subset_size > len(elements):
        return 1, Series([1])
    if subset_size == 0:
        return 1, Series([1])

    # Generate all subsets of the given size from the tuple
    subsets = list(itertools.combinations(elements, subset_size))

    # Calculate the product of the sums of the subsets
    product = 1
    for subset in subsets:
        product *= sum(subset)

    # Return the top_n sums of the subsets as a pandas Series
    return product, Series(sorted(subsets, key=lambda x: sum(x))[:top_n])
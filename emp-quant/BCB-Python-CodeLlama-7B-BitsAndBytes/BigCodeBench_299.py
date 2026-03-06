
import itertools
import math
from pandas import Series

def task_func(elements, subset_size, top_n=2):
    # Generate all subsets of the given size from the tuple
    subsets = list(itertools.combinations(elements, subset_size))

    # Calculate the product of the sums of the subsets
    product = 1
    for subset in subsets:
        product *= sum(subset)

    # Return the top_n sums of the subsets as a pandas Series
    sums = [sum(subset) for subset in subsets]
    return product, Series(sums).nlargest(top_n)
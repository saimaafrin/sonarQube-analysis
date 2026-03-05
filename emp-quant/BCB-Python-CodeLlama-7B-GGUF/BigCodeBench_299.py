
import itertools
import math
from pandas import Series

def task_func(elements, subset_size, top_n=2):
    if subset_size > len(elements):
        return 1, Series([1])
    if subset_size == 0:
        return 1, Series([1])

    subsets = itertools.combinations(elements, subset_size)
    sums = [sum(subset) for subset in subsets]
    product = math.prod(sums)

    return product, Series(sums).nlargest(top_n)
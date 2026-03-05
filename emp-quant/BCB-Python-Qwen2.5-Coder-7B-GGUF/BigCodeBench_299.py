
import itertools
import math
from pandas import Series

def task_func(elements, subset_size, top_n=2):
    if subset_size > len(elements):
        return 1, Series([])
    if subset_size == 0:
        return 1, Series([])
    
    subsets = list(itertools.combinations(elements, subset_size))
    subset_sums = [sum(subset) for subset in subsets]
    product_of_sums = math.prod(subset_sums)
    
    top_n_sums = Series(sorted(subset_sums, reverse=True)[:top_n])
    
    return product_of_sums, top_n_sums
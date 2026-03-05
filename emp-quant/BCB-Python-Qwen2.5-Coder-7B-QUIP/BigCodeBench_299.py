
import itertools
import math
from pandas import Series

def task_func(elements, subset_size, top_n=2):
    # If subset size is larger than the tuple length, return 1
    if subset_size > len(elements):
        return 1, Series([])
    
    # If subset size is 0, return 1
    if subset_size == 0:
        return 1, Series([])
    
    # Generate all subsets of the given size
    subsets = list(itertools.combinations(elements, subset_size))
    
    # Calculate the sum of each subset
    subset_sums = [sum(subset) for subset in subsets]
    
    # Calculate the product of the sums of the subsets
    product_of_sums = math.prod(subset_sums)
    
    # Get the top_n sums of the subsets
    top_n_sums = Series(subset_sums).nsmallest(n=top_n)
    
    return product_of_sums, top_n_sums
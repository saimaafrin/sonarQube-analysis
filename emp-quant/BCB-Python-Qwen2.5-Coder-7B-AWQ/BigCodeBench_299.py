import itertools
import math
from pandas import Series
def task_func(elements, subset_size, top_n=2):
    # Check for edge cases
    if subset_size > len(elements):
        return 1, Series([])
    if subset_size == 0:
        return 1, Series([])
    
    # Generate all subsets of the given size
    subsets = list(itertools.combinations(elements, subset_size))
    
    # Calculate the sum of each subset
    subset_sums = [sum(subset) for subset in subsets]
    
    # Calculate the product of the sums
    product_of_sums = math.prod(subset_sums)
    
    # Get the top_n sums
    top_n_sums = Series(sorted(subset_sums, reverse=True)[:top_n])
    
    return product_of_sums, top_n_sums
elements = (1, 2, 3, 4)
subset_size = 2
top_n = 2
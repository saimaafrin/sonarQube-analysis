from functools import reduce
from itertools import combinations
import numpy as np
def task_func(shape=(3, 3), low=1, high=10, seed=None):
    if high <= low:
        raise ValueError("high must be greater than low")
    
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Generate the matrix with random numbers within the specified range
    matrix = np.random.randint(low, high, size=shape)
    
    # Generate all possible pairs of numbers in the matrix
    pairs = list(combinations(matrix.flatten(), 2))
    
    # Calculate the sum of the products of all pairs
    sum_of_products = reduce(lambda acc, pair: acc + pair[0] * pair[1], pairs, 0)
    
    return sum_of_products, matrix
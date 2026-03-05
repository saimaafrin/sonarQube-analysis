from functools import reduce
from itertools import combinations
import numpy as np
def task_func(shape=(3, 3), low=1, high=10, seed=None):
    """
    Generate a matrix of specified shape and random numbers within a specified range.
    Generate a list of all possible number pairs (all possible combinations of two numbers which are in the matrix) in the matrix.
    Calculate the sum of the products of all pairs.
    """
    if high <= low:
        raise ValueError("high must be greater than low")

    # Generate a matrix of random numbers within the specified range
    matrix = np.random.randint(low, high, size=shape)

    # Generate a list of all possible number pairs in the matrix
    pairs = combinations(matrix.flatten(), 2)

    # Calculate the sum of the products of all pairs
    sum_of_products = reduce(lambda x, y: x * y, pairs)

    return sum_of_products, matrix
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

    np.random.seed(seed)
    matrix = np.random.randint(low, high, size=shape)
    pairs = combinations(matrix.flatten(), 2)
    products = [a * b for a, b in pairs]
    return sum(products), matrix
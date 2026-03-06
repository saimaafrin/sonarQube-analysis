
from functools import reduce
from itertools import combinations
import numpy as np

def task_func(shape=(3, 3), low=1, high=10, seed=None):
    if high <= low:
        raise ValueError("high must be greater than low")

    # Generate a matrix of specified shape and random numbers within the specified range
    matrix = np.random.randint(low, high, size=shape)

    # Calculate the sum of the products of all possible number pairs in the matrix
    sum_of_products = reduce(lambda x, y: x * y, matrix)

    return sum_of_products, matrix
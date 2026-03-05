
from functools import reduce
from itertools import combinations
import numpy as np

def task_func(shape=(3, 3), low=1, high=10, seed=None):
    if high <= low:
        raise ValueError("high must be greater than low")

    np.random.seed(seed)
    matrix = np.random.randint(low, high, size=shape)

    pairs = combinations(matrix.flatten())
    products = reduce(lambda x, y: x * y, pairs)

    return products, matrix
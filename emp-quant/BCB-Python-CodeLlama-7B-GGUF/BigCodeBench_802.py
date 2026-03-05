
import numpy as np
import itertools

def task_func(dimension, seed=42):
    """
    Create a 2D numeric array (matrix) of a given dimension with random integers between 1 and 100, and a flat list of all elements in the matrix.

    Args:
        dimension (int): The dimension of the matrix.
        seed (int, optional): The random seed. Defaults to 42.

    Returns:
        tuple: A tuple containing:
            A 2D numpy array of the given dimension with random integers between 1 and 100.
            A flat list of all elements in the matrix.
    """
    np.random.seed(seed)
    matrix = np.random.randint(1, 100, size=(dimension, dimension))
    flat_list = list(itertools.chain.from_iterable(matrix))
    return matrix, flat_list
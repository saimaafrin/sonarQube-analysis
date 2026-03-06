
import numpy as np
import itertools

def task_func(dimension, seed=42):
    # Generate a 2D numpy array with random integers between 1 and 100
    np_array = np.random.randint(1, 100, size=(dimension, dimension), dtype=int)

    # Flatten the numpy array into a list
    flat_list = list(itertools.chain.from_iterable(np_array))

    # Return a tuple containing the numpy array and the flat list
    return (np_array, flat_list)
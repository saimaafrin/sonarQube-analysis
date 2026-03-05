
import numpy as np
from functools import reduce

def task_func(list_of_pairs):
    return np.array([reduce(lambda x, y: x * y[1], list_of_pairs, 1)])

import numpy as np
from itertools import combinations

def task_func(n):
    if n < 1:
        raise ValueError("n must be greater than 0")
    pairs = list(combinations(range(1, n+1), 2))
    return pairs
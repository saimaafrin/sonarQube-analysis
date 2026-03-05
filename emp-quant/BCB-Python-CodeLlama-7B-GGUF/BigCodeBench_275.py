
import numpy as np
from itertools import combinations

def task_func(n):
    if n < 1:
        raise ValueError("n must be greater than or equal to 1")
    return list(combinations(range(1, n+1), 2))
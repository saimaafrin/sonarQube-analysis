
import numpy as np
from itertools import combinations

def task_func(n):
    if n < 1:
        raise ValueError("n must be greater than or equal to 1")
    num_pairs = int((n * (n + 1)) / 2)
    pairs = []
    for i in range(num_pairs):
        pair = combinations(range(1, n+1), 2)
        pairs.append(pair)
    return pairs
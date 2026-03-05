import numpy as np
from itertools import combinations
def task_func(n):
    if n < 1:
        raise ValueError("Input n must be greater than or equal to 1.")
    
    # Generate all possible combinations of two numbers within the range 1 to n
    pairs = list(combinations(range(1, n + 1), 2))
    
    return pairs
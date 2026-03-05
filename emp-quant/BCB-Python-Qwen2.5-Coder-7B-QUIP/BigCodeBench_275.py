
import numpy as np
from itertools import combinations

def task_func(n):
    if n < 1:
        raise ValueError("Input n must be greater than 0")
    
    # Generate a list of integers from 1 to n
    numbers = list(range(1, n + 1))
    
    # Generate all possible combinations of two numbers
    pairs = list(combinations(numbers, 2))
    
    return pairs
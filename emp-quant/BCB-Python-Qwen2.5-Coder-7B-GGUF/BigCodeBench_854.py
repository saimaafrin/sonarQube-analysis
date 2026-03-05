
from functools import reduce
from itertools import permutations
import math

def task_func(numbers):
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers.")
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All elements in the list must be integers.")
    if any(num < 0 for num in numbers):
        raise ValueError("Input numbers cannot be negative.")
    
    factorial_sums = []
    all_permutations = list(permutations(numbers))
    
    for perm in all_permutations:
        factorial_sum = reduce(lambda x, y: x + math.factorial(y), perm, 0)
        factorial_sums.append(factorial_sum)
    
    return factorial_sums, all_permutations
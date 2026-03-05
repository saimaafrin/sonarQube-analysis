from functools import reduce
from itertools import permutations
import math
def task_func(numbers):
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers.")
    if any(not isinstance(num, int) for num in numbers):
        raise TypeError("All elements in the list must be integers.")
    if any(num < 0 for num in numbers):
        raise ValueError("All numbers must be non-negative.")
    
    if not numbers:
        return [], []
    
    def factorial_sum(perm):
        return sum(math.factorial(num) for num in perm)
    
    permutations_list = list(permutations(numbers))
    factorial_sums = [factorial_sum(perm) for perm in permutations_list]
    
    return factorial_sums, permutations_list

from functools import reduce
from itertools import permutations
import math

def task_func(numbers):
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers.")
    if not all(isinstance(x, int) for x in numbers):
        raise TypeError("All elements in the list must be integers.")
    if any(x < 0 for x in numbers):
        raise ValueError("Input numbers cannot be negative.")
    
    if not numbers:
        return [], []
    
    def factorial(n):
        return math.factorial(n)
    
    def sum_of_factorials(perm):
        return reduce(lambda acc, x: acc + factorial(x), perm, 0)
    
    permutations_list = list(permutations(numbers))
    sums_of_factorials = [sum_of_factorials(perm) for perm in permutations_list]
    
    return sums_of_factorials, permutations_list
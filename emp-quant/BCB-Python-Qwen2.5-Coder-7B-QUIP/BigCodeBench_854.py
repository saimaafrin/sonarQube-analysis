
from functools import reduce
from itertools import permutations
import math

def task_func(numbers):
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers.")
    
    if any(not isinstance(num, int) for num in numbers):
        raise TypeError("All elements in the list must be integers.")
    
    if any(num < 0 for num in numbers):
        raise ValueError("All elements in the list must be non-negative.")
    
    # Calculate the factorial of each number
    fac = [math.factorial(num) for num in numbers]
    
    # Generate all permutations of the list
    perm = list(permutations(numbers))
    
    return fac, perm
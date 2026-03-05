from functools import reduce
from itertools import permutations
import math
def task_func(numbers):
    # Check if the input is a list of integers
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("Input must be a list of integers")
    
    # Check if all numbers are non-negative
    if any(num < 0 for num in numbers):
        raise ValueError("All numbers must be non-negative")
    
    # Calculate the factorial of each number
    factorials = [math.factorial(num) for num in numbers]
    
    # Generate all permutations of the numbers
    perms = list(permutations(numbers))
    
    # Calculate the sum of factorials for each permutation
    sum_of_factorials = [reduce(lambda x, y: x + y, [factorials[nums.index(n)] for n in perm]) for perm in perms]
    
    return sum_of_factorials, perms
from functools import reduce
from itertools import permutations
import math
def task_func(numbers):
    """
    Generate all permutations of a given list of numbers and calculate the sum of the factorials of each number in each permutation.
    If an empty list is given, the function returns empty lists.
    """
    if not isinstance(numbers, list):
        raise TypeError("numbers must be a list of integers")
    if any(x < 0 for x in numbers):
        raise ValueError("input numbers must be non-negative")

    # Calculate factorials
    factorials = [math.factorial(x) for x in numbers]

    # Generate permutations
    permutations = list(permutations(numbers))

    # Calculate sums of factorials for each permutation
    sums = [sum(factorials[i] for i in perm) for perm in permutations]

    return sums, permutations
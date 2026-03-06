
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
    if any(n < 0 for n in numbers):
        raise ValueError("input numbers must be non-negative")

    # Calculate the factorials of each number
    factorials = [math.factorial(n) for n in numbers]

    # Calculate the sums of the factorials for each permutation
    permutation_sums = [sum(factorials[i] for i in range(len(numbers))) for _ in permutations(numbers)]

    return permutation_sums, [list(p) for p in permutations(numbers)]
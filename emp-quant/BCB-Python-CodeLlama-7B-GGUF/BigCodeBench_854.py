
from functools import reduce
from itertools import permutations
import math

def task_func(numbers):
    """
    Generate all permutations of a given list of numbers and calculate the sum of the factorials of each number in each permutation.

    Parameters
    ----------
    numbers : list of int
        The list of numbers to generate permutations for.

    Returns
    -------
    list of int
        A list containing the sums of the factorials of each number in each permutation.
    list of list of int
        A list containing all permutations of numbers.

    Raises
    ------
    TypeError
        If numbers is not a list of integers.
    ValueError
        If input numbers are negative.
    """
    if not isinstance(numbers, list):
        raise TypeError("numbers must be a list of integers")
    if any(num < 0 for num in numbers):
        raise ValueError("input numbers must be non-negative")

    # Calculate the factorial of each number
    factorials = [math.factorial(num) for num in numbers]

    # Calculate the sum of the factorials of each number in each permutation
    permutation_sums = [sum(factorials[i:] + factorials[:i]) for i in range(len(numbers))]

    # Generate all permutations of numbers
    permutations_list = [list(permutation) for permutation in permutations(numbers)]

    return permutation_sums, permutations_list
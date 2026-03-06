
from functools import reduce
from itertools import permutations
import math

def task_func(numbers):
    if not isinstance(numbers, list) or not all(isinstance(x, int) for x in numbers):
        raise TypeError("Input must be a list of integers.")
    if any(x < 0 for x in numbers):
        raise ValueError("All numbers in the list must be non-negative.")

    def factorial(n):
        return math.factorial(n)

    def sum_of_factorials(perm):
        return sum(factorial(x) for x in perm)

    permutations_list = list(permutations(numbers))
    sum_of_factorials_list = [sum_of_factorials(perm) for perm in permutations_list]

    return sum_of_factorials_list, permutations_list
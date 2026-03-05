
from functools import reduce
from itertools import permutations
import math

def task_func(numbers):
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers")
    if any(map(lambda x: x < 0, numbers)):
        raise ValueError("Input numbers cannot be negative")
    factorials = map(math.factorial, numbers)
    sums = map(reduce(lambda x, y: x + y, factorials), range(len(numbers)))
    permutations = permutations(numbers)
    return sums, permutations
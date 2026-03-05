import random
import math
def task_func(range_start=1, range_end=100, pairs_count=10, random_seed=None):
    """
    Generates a generator object that produces tuples in the format
    (num1, num2, square root of absolute difference).
    
    :param range_start: The start of the range for generating random numbers.
    :param range_end: The end of the range for generating random numbers.
    :param pairs_count: The number of pairs to generate.
    :param random_seed: The seed for the random number generator for reproducibility.
    :return: A generator object.
    """
    if random_seed is not None:
        random.seed(random_seed)
    
    for _ in range(pairs_count):
        num1 = random.randint(range_start, range_end)
        num2 = random.randint(range_start, range_end)
        diff = abs(num1 - num2)
        yield (num1, num2, math.sqrt(diff))
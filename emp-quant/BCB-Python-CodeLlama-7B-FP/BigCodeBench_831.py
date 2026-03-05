import random
import math
def task_func(range_start=1, range_end=100, pairs_count=10, random_seed=None):
    """
    Generates a sequence of tuples. Each tuple contains two random numbers and the square root of their absolute difference.
    A random seed is used to have reproducability in the outputs.
    """
    if random_seed is not None:
        random.seed(random_seed)
    for _ in range(pairs_count):
        num1 = random.randint(range_start, range_end)
        num2 = random.randint(range_start, range_end)
        yield (num1, num2, math.sqrt(abs(num1 - num2)))
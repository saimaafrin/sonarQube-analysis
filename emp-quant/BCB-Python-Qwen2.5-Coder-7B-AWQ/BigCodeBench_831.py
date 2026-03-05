import random
import math
def task_func(range_start=1, range_end=100, pairs_count=10, random_seed=None):
    """
    generator: A generator object that produces tuples in the format
    (num1, num2, square root of absolute difference).
    """
    if random_seed is not None:
        random.seed(random_seed)
    
    for _ in range(pairs_count):
        num1 = random.randint(range_start, range_end)
        num2 = random.randint(range_start, range_end)
        abs_diff = abs(num1 - num2)
        sqrt_diff = math.sqrt(abs_diff)
        yield (num1, num2, sqrt_diff)
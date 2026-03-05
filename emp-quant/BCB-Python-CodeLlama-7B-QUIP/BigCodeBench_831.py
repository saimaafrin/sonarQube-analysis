
import random
import math

def task_func(range_start=1, range_end=100, pairs_count=10, random_seed=None):
    if random_seed:
        random.seed(random_seed)
    nums = [random.randint(range_start, range_end) for i in range(pairs_count)]
    pairs = [(nums[i], nums[i+1], math.sqrt(abs(nums[i] - nums[i+1]))) for i in range(pairs_count-1)]
    return iter(pairs)

pairs = task_func(1, 3, pairs_count=25, random_seed=14)
print(next(pairs))
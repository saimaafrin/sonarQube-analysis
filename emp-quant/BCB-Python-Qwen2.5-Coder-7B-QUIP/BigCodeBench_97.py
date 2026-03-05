
import math
import itertools
from functools import reduce

def task_func(numbers):
    total_log_sum = 0.0
    for length in range(1, len(numbers) + 1):
        for combo in itertools.combinations(numbers, length):
            product = reduce(lambda x, y: x * y, combo, 1)
            total_log_sum += math.log(product)
    return total_log_sum
import math
import itertools
from functools import reduce
def task_func(numbers):
    total_sum = 0.0
    for r in range(1, len(numbers) + 1):
        for combination in itertools.combinations(numbers, r):
            product = reduce(lambda x, y: x * y, combination)
            log_product = math.log(product)
            total_sum += log_product
    return total_sum
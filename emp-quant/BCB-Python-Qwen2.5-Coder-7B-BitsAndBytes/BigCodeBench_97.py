
import math
import itertools
from functools import reduce

def task_func(numbers):
    total_sum = 0.0
    # Iterate over all possible lengths of combinations
    for r in range(1, len(numbers) + 1):
        # Generate all combinations of the current length
        for combo in itertools.combinations(numbers, r):
            # Calculate the product of the combination
            product = reduce(lambda x, y: x * y, combo)
            # Compute the logarithm of the product
            log_product = math.log(product)
            # Add the logarithm to the total sum
            total_sum += log_product
    return total_sum
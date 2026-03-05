
import itertools
import math

def task_func(x):
    # Calculate the cosine of each value and sum them up
    def cosine_sum(key):
        return sum(math.cos(val) for val in x[key])

    # Find the key pair with the highest sum of cosine values
    max_cosine_sum = -float('inf')
    best_pair = None
    for key1, key2 in itertools.combinations(x, 2):
        sum_cosine = cosine_sum(key1) + cosine_sum(key2)
        if sum_cosine > max_cosine_sum:
            max_cosine_sum = sum_cosine
            best_pair = (key1, key2)

    return best_pair
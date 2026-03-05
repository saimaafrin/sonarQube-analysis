
import itertools
import math

def task_func(x):
    # Calculate the cosine of each value in the dictionary
    cos_values = [math.cos(value) for value in x.values()]

    # Find the key pair with the highest sum of cosine values
    key_pair = max(itertools.product(x.keys(), repeat=2), key=lambda pair: sum(cos_values[pair[0]], cos_values[pair[1]]))

    return key_pair

print(task_func(x))  # Output: ('a', 'b')

import itertools
import math

def task_func(x):
    # Calculate the cosine of each value in the dictionary
    cos_values = {key: math.cos(value) for key, value in x.items()}

    # Calculate the sum of the cosines of each key
    sum_cos_values = {key: sum(cos_values[key]) for key in cos_values}

    # Find the key with the highest sum of cosines
    max_key = max(sum_cos_values, key=sum_cos_values.get)

    # Return the pair of keys with the highest sum of cosines
    return (max_key, sum_cos_values[max_key])
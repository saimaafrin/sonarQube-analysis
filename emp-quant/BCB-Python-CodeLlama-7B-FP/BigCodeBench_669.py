import itertools
import math
def task_func(x):
    """
    Find the key pair in a dictionary, x, which has the highest sum of the cosine of each of its values.
    The function should output with:
        tuple: The pair of keys with the highest sum of the cosine of their values.
    """
    # Initialize the maximum sum and the corresponding keys
    max_sum = 0
    max_keys = None

    # Iterate over the key-value pairs in the dictionary
    for key, value in x.items():
        # Calculate the cosine of the value
        cos_value = math.cos(value)

        # Calculate the sum of the cosine of the value and the current maximum sum
        sum_cos_value = cos_value + max_sum

        # If the new sum is greater than the current maximum sum, update the maximum sum and the corresponding keys
        if sum_cos_value > max_sum:
            max_sum = sum_cos_value
            max_keys = (key,)

    # Return the pair of keys with the highest sum of the cosine of their values
    return max_keys
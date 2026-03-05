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

        # Calculate the sum of the cosine of the value and the previous values
        sum_cos_values = max_sum + cos_value

        # Check if the current sum is greater than the maximum sum
        if sum_cos_values > max_sum:
            # Update the maximum sum and the corresponding keys
            max_sum = sum_cos_values
            max_keys = (key,)

    # Return the pair of keys with the highest sum of the cosine of their values
    return max_keys
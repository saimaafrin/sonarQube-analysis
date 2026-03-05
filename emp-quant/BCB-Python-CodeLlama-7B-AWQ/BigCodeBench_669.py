import itertools
import math
def task_func(x):
    """
    Find the key pair in a dictionary, x, which has the highest sum of the cosine of each of its values.
    :param x: dictionary
    :return: tuple: The pair of keys with the highest sum of the cosine of their values.
    """
    # Initialize the maximum sum and the corresponding keys
    max_sum = 0
    max_keys = None

    # Iterate over the keys and values in the dictionary
    for key, value in x.items():
        # Calculate the cosine of the value
        cos_value = math.cos(value)

        # Update the maximum sum and keys if the current sum is greater than the previous maximum
        if max_sum < cos_value:
            max_sum = cos_value
            max_keys = (key,)

    # Return the maximum sum and keys
    return max_keys
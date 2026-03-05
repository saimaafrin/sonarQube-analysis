import numpy as np
from itertools import zip_longest
def task_func(l1, l2, THRESHOLD = 0.5):
    """
    Alternates elements from two numeric lists, calculates the absolute difference of each element from a predefined threshold, and returns the element closest to this threshold.
    """
    # Create a list of tuples containing the elements from the two lists and their corresponding absolute differences from the threshold
    diff_list = [(abs(x - y), x, y) for x, y in zip_longest(l1, l2)]

    # Sort the list by the absolute difference from the threshold
    diff_list.sort(key=lambda x: x[0])

    # Return the element from the combined list that is closest to the threshold of 0.5
    return diff_list[0][1] if diff_list else None
l1 = [1, 2, 3, 4, 5]
l2 = [1.1, 2.2, 3.3, 4.4, 5.5]
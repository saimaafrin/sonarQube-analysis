import numpy as np
from itertools import zip_longest
def task_func(l1, l2, THRESHOLD = 0.5):
    """
    Alternates elements from two numeric lists, calculates the absolute difference of each element from a predefined threshold, and returns the element closest to this threshold.
    """
    # Calculate the absolute difference between each element in l1 and l2
    diffs = [abs(x - y) for x, y in zip_longest(l1, l2)]

    # Find the element closest to the threshold
    closest = min(diffs, key=lambda x: abs(x - THRESHOLD))

    return closest
l1 = [1, 2, 3, 4, 5]
l2 = [1, 2, 3, 4, 5]
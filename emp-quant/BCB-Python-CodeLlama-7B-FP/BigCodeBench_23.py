import numpy as np
from itertools import zip_longest
def task_func(l1, l2, THRESHOLD = 0.5):
    """
    Alternates elements from two numeric lists, calculates the absolute difference of each element from a predefined threshold, and returns the element closest to this threshold.
    If l1 and l2 are of different lengths, elements from the longer list without a corresponding pair in the shorter list will not be paired with 'None'.
    Only existing numeric elements are considered. The threshold is fixed at 0.5. Adjustments to the threshold require changes to the THRESHOLD constant.
    """
    # Combine the two lists into a single list of tuples
    combined_list = list(zip_longest(l1, l2))

    # Filter out non-numeric elements
    filtered_list = [element for element in combined_list if isinstance(element, (int, float))]

    # Calculate the absolute difference between each element and the threshold
    absolute_differences = [abs(element - THRESHOLD) for element in filtered_list]

    # Find the element with the smallest absolute difference
    closest_element = min(filtered_list, key=absolute_differences.index)

    return closest_element
l1 = [1, 2, 3, 4, 5]
l2 = [1.5, 2.5, 3.5, 4.5, 5.5]
THRESHOLD = 0.25
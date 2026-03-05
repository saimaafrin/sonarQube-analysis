import numpy as np
from itertools import zip_longest
def task_func(l1, l2, THRESHOLD = 0.5):
    # Initialize a variable to store the closest element
    closest_element = None
    # Initialize a variable to store the minimum difference
    min_diff = float('inf')
    
    # Use zip_longest to pair elements from both lists, filling missing values with None
    for a, b in zip_longest(l1, l2):
        # Check if both elements are numeric
        if a is not None and b is not None:
            # Calculate the absolute difference from the threshold
            diff = abs(a - b)
            # Check if the current difference is smaller than the minimum difference found so far
            if diff < min_diff:
                min_diff = diff
                closest_element = a if diff < abs(a - THRESHOLD) else b
    
    # Return the element closest to the threshold
    return closest_element
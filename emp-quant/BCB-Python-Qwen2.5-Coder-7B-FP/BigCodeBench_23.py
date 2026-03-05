import numpy as np
from itertools import zip_longest
def task_func(l1, l2, THRESHOLD = 0.5):
    # Initialize a variable to store the closest element
    closest_element = None
    # Initialize a variable to store the minimum difference
    min_diff = float('inf')
    
    # Use zip_longest to handle lists of different lengths
    for a, b in zip_longest(l1, l2):
        # Check if both elements are numeric
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            # Calculate the absolute difference from the threshold
            diff = abs(a - THRESHOLD)
            # Check if the current difference is smaller than the minimum difference
            if diff < min_diff:
                min_diff = diff
                closest_element = a
            # Calculate the absolute difference from the threshold
            diff = abs(b - THRESHOLD)
            # Check if the current difference is smaller than the minimum difference
            if diff < min_diff:
                min_diff = diff
                closest_element = b
                
    return closest_element
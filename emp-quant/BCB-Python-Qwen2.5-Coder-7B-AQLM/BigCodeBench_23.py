
import numpy as np
from itertools import zip_longest

def task_func(l1, l2, THRESHOLD = 0.5):
    # Initialize variables to store the closest element and its difference
    closest_element = None
    min_diff = float('inf')
    
    # Iterate over the combined list of l1 and l2 using zip_longest
    for a, b in zip_longest(l1, l2):
        # Check if both elements are numeric
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            # Calculate the absolute differences from the threshold
            diff_a = abs(a - THRESHOLD)
            diff_b = abs(b - THRESHOLD)
            
            # Update the closest element if the current one is closer
            if diff_a < min_diff:
                closest_element = a
                min_diff = diff_a
            if diff_b < min_diff:
                closest_element = b
                min_diff = diff_b
    
    return closest_element
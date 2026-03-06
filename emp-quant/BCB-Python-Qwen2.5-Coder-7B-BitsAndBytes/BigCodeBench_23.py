
import numpy as np
from itertools import zip_longest

def task_func(l1, l2, THRESHOLD = 0.5):
    # Combine the two lists using zip_longest to handle unequal lengths
    combined = zip_longest(l1, l2)
    
    # Initialize variables to store the minimum difference and the corresponding element
    min_diff = float('inf')
    closest_element = None
    
    # Iterate through the combined pairs
    for a, b in combined:
        if a is not None and b is not None:
            # Calculate the absolute differences from the threshold
            diff_a = abs(a - THRESHOLD)
            diff_b = abs(b - THRESHOLD)
            
            # Update the closest element based on the smallest difference
            if diff_a < min_diff:
                min_diff = diff_a
                closest_element = a
            if diff_b < min_diff:
                min_diff = diff_b
                closest_element = b
    
    return closest_element
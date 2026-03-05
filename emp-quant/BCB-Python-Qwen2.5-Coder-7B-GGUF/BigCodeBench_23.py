
import numpy as np
from itertools import zip_longest

def task_func(l1, l2, THRESHOLD = 0.5):
    # Initialize a variable to store the closest element
    closest_element = None
    # Initialize a variable to store the minimum difference
    min_diff = float('inf')
    
    # Use zip_longest to handle lists of different lengths
    for num1, num2 in zip_longest(l1, l2):
        # Check if both elements are numeric
        if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
            # Calculate the absolute difference from the threshold
            diff1 = abs(num1 - THRESHOLD)
            diff2 = abs(num2 - THRESHOLD)
            # Update the closest element if a closer one is found
            if diff1 < min_diff:
                closest_element = num1
                min_diff = diff1
            if diff2 < min_diff:
                closest_element = num2
                min_diff = diff2
    
    return closest_element
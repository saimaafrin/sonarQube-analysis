
import numpy as np
from itertools import zip_longest

def task_func(l1, l2, THRESHOLD=0.5):
    # Combine the two lists, filling missing values with None
    combined = list(zip_longest(l1, l2))
    
    # Filter out non-numeric values and calculate the absolute difference from the threshold
    diff = [(x - THRESHOLD) if x is not None else None for x in [np.abs(a - THRESHOLD) for a in [item for sublist in combined for item in sublist] if isinstance(item, (int, float))]]
    
    # Find the minimum absolute difference
    min_diff = min(diff, key=lambda x: x if x is not None else float('inf'))
    
    # Return the element closest to the threshold
    return min_diff
import numpy as np
import math
def task_func(L):
    # Flatten the nested list into a single list
    flattened_list = [item for sublist in L for item in sublist]
    
    # Sort the flattened list
    sorted_list = sorted(flattened_list)
    
    # Calculate the median
    n = len(sorted_list)
    if n % 2 == 1:
        # If the number of elements is odd, return the middle element
        median = sorted_list[n // 2]
    else:
        # If the number of elements is even, return the average of the two middle elements
        median = (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2
    
    return median
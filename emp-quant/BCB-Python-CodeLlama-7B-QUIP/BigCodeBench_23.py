
import numpy as np
from itertools import zip_longest

def task_func(l1, l2, THRESHOLD = 0.5):
    # Calculate the absolute difference between corresponding elements in l1 and l2
    diffs = np.abs(np.subtract(l1, l2))
    # Find the index of the element in diffs that is closest to the threshold
    closest_index = np.argmin(diffs)
    # Return the element from the combined list that is closest to the threshold
    return l1[closest_index]
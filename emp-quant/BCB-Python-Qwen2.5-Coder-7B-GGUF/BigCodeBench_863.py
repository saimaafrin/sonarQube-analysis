
import numpy as np
import math
# Constants
POSSIBLE_NUMBERS = np.arange(1, 11)

def task_func(list_of_lists):
    sums = []
    for lst in list_of_lists:
        # Calculate the sum of squares of the first len(lst) elements from POSSIBLE_NUMBERS
        sum_of_squares = sum(POSSIBLE_NUMBERS[:len(lst)] ** 2)
        sums.append(sum_of_squares)
    return sums
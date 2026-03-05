
import numpy as np
import math
# Constants
POSSIBLE_NUMBERS = np.arange(1, 11)

def task_func(list_of_lists):
    sums = []
    for lst in list_of_lists:
        num_elements = len(lst)
        selected_numbers = POSSIBLE_NUMBERS[:num_elements]
        sum_of_squares = np.sum(np.square(selected_numbers))
        sums.append(sum_of_squares)
    return sums
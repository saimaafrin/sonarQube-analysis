
import numpy as np
import math
# Constants
POSSIBLE_NUMBERS = np.arange(1, 11)

def task_func(list_of_lists):
    sums = []
    for lst in list_of_lists:
        # Determine the number of elements to consider from POSSIBLE_NUMBERS
        num_elements = len(lst)
        # Get the first 'num_elements' numbers from POSSIBLE_NUMBERS
        selected_numbers = POSSIBLE_NUMBERS[:num_elements]
        # Calculate the sum of squares
        sum_of_squares = np.sum(selected_numbers ** 2)
        sums.append(sum_of_squares)
    return sums
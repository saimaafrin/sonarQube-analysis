
import numpy as np
import math
# Constants
POSSIBLE_NUMBERS = np.arange(1, 11)
def task_func(list_of_lists):
    # Initialize the sums
    sums = []
    # Loop through each list in list_of_lists
    for i in range(len(list_of_lists)):
        # Get the current list
        current_list = list_of_lists[i]
        # Calculate the sum of squares
        sum_of_squares = 0
        for j in range(len(current_list)):
            sum_of_squares += math.pow(POSSIBLE_NUMBERS[j], 2)
        # Add the sum to the sums list
        sums.append(sum_of_squares)
    # Return the sums
    return sums
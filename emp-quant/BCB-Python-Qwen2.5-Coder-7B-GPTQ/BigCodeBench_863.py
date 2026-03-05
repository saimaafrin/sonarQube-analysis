import numpy as np
import math
POSSIBLE_NUMBERS = np.arange(1, 11)
def task_func(list_of_lists):
    sums = []
    for lst in list_of_lists:
        # Calculate the sum of squares of the first 'n' elements from POSSIBLE_NUMBERS
        n = min(len(lst), len(POSSIBLE_NUMBERS))
        sum_of_squares = sum(POSSIBLE_NUMBERS[:n]**2)
        sums.append(sum_of_squares)
    return sums
list_of_lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9, 10], [11, 12, 13]]
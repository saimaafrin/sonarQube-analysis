
import numpy as np
import math

# Constants
POSSIBLE_NUMBERS = np.arange(1, 11)

def task_func(list_of_lists):
    sums = []
    for lst in list_of_lists:
        sum_of_squares = 0
        for i in range(len(lst)):
            sum_of_squares += math.pow(POSSIBLE_NUMBERS[i], 2)
        sums.append(sum_of_squares)
    return sums
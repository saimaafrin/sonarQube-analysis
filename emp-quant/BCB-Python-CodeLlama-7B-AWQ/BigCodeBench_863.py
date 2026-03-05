import numpy as np
import math
POSSIBLE_NUMBERS = np.arange(1, 11)
def task_func(list_of_lists):
    """
    Calculate the sum of the squares of numbers from a predefined range (POSSIBLE_NUMBERS) for each list in list_of_lists.
    The number of elements considered from POSSIBLE_NUMBERS is determined by the length of each list.
    The function should output with:
        sums (list): A list of sums of squares.
    """
    sums = []
    for lst in list_of_lists:
        sum_of_squares = 0
        for i in range(len(lst)):
            sum_of_squares += (POSSIBLE_NUMBERS[i] ** 2)
        sums.append(sum_of_squares)
    return sums
list_of_lists = [[1, 2, 3], [4, 5, 6, 7], [8, 9]]
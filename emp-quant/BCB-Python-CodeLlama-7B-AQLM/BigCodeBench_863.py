import numpy as np
import math
def task_func(list_of_lists):
    """
    Calculate the sum of the squares of numbers from a predefined range (POSSIBLE_NUMBERS) 
    for each list in list_of_lists. The number of elements considered from POSSIBLE_NUMBERS 
    is determined by the length of each list.

    Parameters:
    - list_of_lists (list): A list of lists, each representing a set of numbers.

    Returns:
    - sums (list): A list of sums of squares.

    Requirements:
    - numpy
    - math

    Example:
    >>> sums = task_func([[1, 2, 3], [4, 5]])
    >>> print(sums)
    [14.0, 5.0]
    """
    sums = []
    for list_of_numbers in list_of_lists:
        sum_of_squares = 0
        for number in list_of_numbers:
            sum_of_squares += math.pow(number, 2)
        sums.append(sum_of_squares)
    return sums
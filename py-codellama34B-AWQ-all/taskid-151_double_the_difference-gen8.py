from typing import List

def double_the_difference(lst: List[float]) -> int:
    """
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    >>> double_the_difference([1, 3, 2, 0])
    10
    >>> double_the_difference([-1, -2, 0])
    0
    >>> double_the_difference([9, -2])
    81
    >>> double_the_difference([0])
    0
   
    If the input list is empty, return 0.
    """


    # filter out negative numbers, non-integers, and 0
    # we don't want to square them since they are even
    # and won't contribute anything to the final sum
    filtered_list = [x for x in lst if x > 0 and x % 1 == 0]
    
    sum_of_squares = 0

    for num in filtered_list:
        if num % 2 != 0:
            sum_of_squares += num ** 2

    return sum_of_squares

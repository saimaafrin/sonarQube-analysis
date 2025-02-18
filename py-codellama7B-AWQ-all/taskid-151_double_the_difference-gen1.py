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

    if len(lst) == 0:
        return 0
    else:
        lst = [abs(x) for x in lst]
        lst = [int(x) for x in lst]
        lst = [x for x in lst if x%2 == 1]
        lst = [x*x for x in lst]
        return sum(lst)

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

    a = lst[::2]
    b = lst[1::2]
    return sum(pow(abs(i-j), 2) for i,j in zip(a, b) if (i >= 0 and j >= 0) and (isinstance(i, int) and isinstance(j, int)))

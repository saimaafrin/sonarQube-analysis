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

    
    # Your code here
    total = 0
    for element in lst:
        if element % 2 == 0:
            total += element ** 2
    return total

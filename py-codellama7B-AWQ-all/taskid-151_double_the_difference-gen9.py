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

    lst = [float(i) for i in lst]
    lst = sorted(lst)
    if abs(lst[0]) < 0.00001:
        lst = lst[1:]
    if abs(lst[-1]) < 0.00001:
        lst = lst[:-1]
    return (lst[1]-lst[0])*2

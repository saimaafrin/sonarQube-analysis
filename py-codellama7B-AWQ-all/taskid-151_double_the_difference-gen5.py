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

    lst_len = len(lst)
    if lst_len == 0:
        return 0
    else:
        max_val = lst[0]
        min_val = lst[0]
        for i in range(1, lst_len):
            if lst[i] > max_val:
                max_val = lst[i]
            if lst[i] < min_val:
                min_val = lst[i]

        return int((max_val - min_val) * 2)

from typing import List

def solution(lst: List[int]) -> int:
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    >>> solution([5, 8, 7, 1])
    12
    >>> solution([3, 3, 3, 3, 3])
    9
    >>> solution([30, 13, 24, 321])
    0
    """

    
    sum_of_odd_even = 0
    for idx, val in enumerate(lst):
        if idx % 2 == 0:
            if val % 2 != 0:
                sum_of_odd_even += val
    return sum_of_odd_even

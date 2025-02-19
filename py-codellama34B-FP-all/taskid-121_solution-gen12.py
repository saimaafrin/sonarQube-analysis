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


    if len(lst) == 0:
        raise ValueError('list must not be empty')
    
    result = 0
    
    for i in range(len(lst)):
        if i % 2 == 0 and lst[i] % 2 != 0:
            result += lst[i]

    return result

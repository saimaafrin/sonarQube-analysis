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

    # Your code here
    result = 0
    for i, val in enumerate(lst):
        if i % 2 == 0 and val % 2 != 0:
            result += val
    return result

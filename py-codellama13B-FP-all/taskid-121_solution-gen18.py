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

    if not lst:
        raise ValueError("list cannot be empty")

    sum_of_odd = 0
    for i, v in enumerate(lst):
        if v % 2 != 0 and i % 2 == 0:
            sum_of_odd += v

    return sum_of_odd

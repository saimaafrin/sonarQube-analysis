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

    # if the length is odd, add the last element to the result
    if len(lst) % 2 == 1:
        lst.append(0)

    result = 0

    for i, num in enumerate(lst):
        if i % 2 == 0 and num % 2 != 0:
            result += num

    return result

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

    # your code here
    sum = 0
    for i, num in enumerate(lst):
        if i%2==0:
            if num%2!=0:
                sum += num
    return sum

    # second way
    return sum(num for i, num in enumerate(lst) if num%2 != 0 and i%2==0)

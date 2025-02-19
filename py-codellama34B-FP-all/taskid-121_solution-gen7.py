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

    odd_elements = []
    for index, element in enumerate(lst):
        if index % 2 == 0 and element % 2 == 1:
            odd_elements.append(element)

    return sum(odd_elements)

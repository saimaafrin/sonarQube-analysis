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

    odd_positions = [i for i in range(len(lst)) if lst[i] % 2 == 1]
    even_positions = [i for i in range(len(lst)) if lst[i] % 2 == 0]
    odd_positions = [lst[i] for i in odd_positions]
    even_positions = [lst[i] for i in even_positions]
    return sum(odd_positions) + sum(even_positions)

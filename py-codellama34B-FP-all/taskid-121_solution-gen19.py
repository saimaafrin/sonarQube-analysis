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


    odd_indexes = [0, 2, 4, 6, 8]
    odd_numbers = [number for number in lst if number % 2 == 1]
    return sum([odd_numbers[i] for i in odd_indexes])

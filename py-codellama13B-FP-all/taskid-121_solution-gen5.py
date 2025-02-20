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

    # first we filter only the odd numbers
    odd_numbers = list(filter(lambda x: x % 2 != 0, lst))
    # then we get only the even positions
    even_positions = [x for x in range(len(lst)) if x % 2 == 0]
    # then we filter the odd numbers to get the ones in even positions
    evens_only = list(filter(lambda x: x in odd_numbers, even_positions))
    # then we sum the odd numbers in even positions
    result = sum(evens_only)
    
    return result

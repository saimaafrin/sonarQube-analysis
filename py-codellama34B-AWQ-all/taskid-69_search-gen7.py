from typing import List

def search(lst: List[int]) -> int:
    """
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
    >>> search([4, 1, 2, 2, 3, 1])
    2
    >>> search([1, 2, 2, 3, 3, 3, 4, 4, 4])
    3
    >>> search([5, 5, 4, 4, 4])
    -1
    """

    freq_map = {}
    for n in lst:
        if n in freq_map:
            freq_map[n] += 1
        else:
            freq_map[n] = 1
    for n in freq_map.keys():
        if n > 0 and freq_map[n] >= n:
            return n
    return -1

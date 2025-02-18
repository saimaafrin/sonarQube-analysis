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

    d: dict = {}
    max_freq: int = 0
    max_el: int = -1
    for el in lst:
        if el in d:
            d[el] += 1
        else:
            d[el] = 1
        if d[el] > max_freq:
            max_freq = d[el]
            max_el = el
    if max_freq < 2:
        return -1
    return max_el

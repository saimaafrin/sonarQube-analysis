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

    d = {}
    for item in lst:
        if item in d:
            d[item] += 1
        else:
            d[item] = 1
        if item > 1 and d[item] >= item:
            return item

    keys = list(d.keys())
    keys.sort(reverse=True)

    for i in keys:
        if d[i] > 1 and i > 1:
            return i
    return -1

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

    # The function should return -1 if no value is found
    # Otherwise it should return the value
    max_freq = -1
    max_val = -1
    for val in set(lst):
        if lst.count(val) >= val > max_freq:
            max_freq = lst.count(val)
            max_val = val

    return max_val

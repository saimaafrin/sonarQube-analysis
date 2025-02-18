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

    # return the maximum integer that is greater than 0 and has a frequency greater than or equal to its value
    max_freq = -1
    max_int = -1
    for int_ in lst:
        freq = lst.count(int_)
        if freq > max_freq and freq >= int_ and int_ > 0:
            max_freq = freq
            max_int = int_
    if max_freq >= max_int:
        return -1
    return max_int

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

    count = {}
    max_freq = 0
    res = 0

    for i in lst:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
        max_freq = max(max_freq, count[i])

    for k, v in count.items():
        if v == max_freq:
            res = k
            break
    if res == 0:
        return -1
    else:
        return res

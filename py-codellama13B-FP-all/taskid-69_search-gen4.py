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

    # 0) Check if the list is empty
    if len(lst) == 0:
        return -1
    # 1) Initialize max_freq and the max_val
    max_freq = 0
    max_val = -1
    # 2) Iterate over the list and compare the frequency of each number to the current max_freq
    for i in lst:
        freq = lst.count(i)
        if freq >= max_freq:
            max_freq = freq
            max_val = i
    # 3) Check if the max_val is greater than 0
    if max_val > 0:
        return max_val
    # 4) Otherwise return -1
    else:
        return -1

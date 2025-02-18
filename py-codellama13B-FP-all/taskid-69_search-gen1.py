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

    # convert list to a dictionary
    counts = {}
    for num in lst:
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1
    # find the maximum integer that is greater than 0
    # and has a frequency greater than or equal to its value.
    for num, freq in counts.items():
        if num > 0 and freq >= num:
            return num
    return -1

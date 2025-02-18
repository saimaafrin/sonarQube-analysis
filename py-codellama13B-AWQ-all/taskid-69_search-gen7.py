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

    # first, sort the list
    lst.sort()
    # find the index of the first element that is greater than its frequency in the list
    i = 1
    while i < len(lst):
        if lst[i] > lst[i-1]:
            return lst[i-1]
        else:
            i += 1
    # if all elements have the same frequency, return the max frequency, or -1 if no max exists
    if len(set(lst)) == 1:
        return lst[0]
    else:
        return -1

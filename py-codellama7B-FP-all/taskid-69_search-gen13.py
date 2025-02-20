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

    # TODO - you fill in here.
    # count the frequency of each number
    count = {}
    for i in lst:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    # get the maximum value with frequency >= value
    for i in count:
        if count[i] >= i and i > 0:
            return i
    
    return -1

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

    # create an empty dictionary
    freq = {}
    # loop through the list
    for n in lst:
        # if n is not in the dictionary add it with a value of 1
        if n not in freq:
            freq[n] = 1
        # if n is already in the dictionary, increment its value
        else:
            freq[n] += 1
    # loop through the dictionary
    for n in freq:
        # if the value of n is greater than or equal to the key, return n
        if freq[n] >= n and n > 0:
            return n
    # if no value is found return -1
    return -1

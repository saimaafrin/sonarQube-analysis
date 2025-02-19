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


    # create dict to hold occurences
    occurences = {}
    for i in lst:
        if i not in occurences:
            occurences[i] = 1
        else:
            occurences[i] += 1

    # find the greatest integer that is greater than 0
    max_value = -1
    for key in occurences:
        if key > max_value and occurences[key] >= key:
            max_value = key

    # if no integer is found, return -1
    if max_value == -1:
        return -1
    else:
        return max_value

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

    # Write your code here

    max_value = -1
    value_occurrence_map = {}
    for value in lst:
        if value > max_value:
            max_value = value
        if value not in value_occurrence_map:
            value_occurrence_map[value] = 1
        else:
            value_occurrence_map[value] += 1

    for value in value_occurrence_map:
        if value_occurrence_map[value] >= value:
            return value
    return -1

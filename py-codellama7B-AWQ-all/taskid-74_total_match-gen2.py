from typing import List

def total_match(lst1: List[str], lst2: List[str]) -> List[str]:
    """
    Write a function that accepts two lists of strings and returns the list that has 
    total number of chars in the all strings of the list less than the other list.

    if the two lists have the same number of chars, return the first list.

    Examples
    >>> total_match([], [])
    []
    >>> total_match(['hi', 'admin'], ['hI', 'Hi'])
    ['hI', 'Hi']
    >>> total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project'])
    ['hi', 'admin']
    >>> total_match(['hi', 'admin'], ['hI', 'hi', 'hi'])
    ['hI', 'hi', 'hi']
    >>> total_match(['4'], ['1', '2', '3', '4', '5'])
    ['4']
    """

    lst1.sort(key=len)
    lst2.sort(key=len)
    # if both lists have same number of chars, return first list
    if len(lst1) == len(lst2) and len(lst1) > 0:
        return lst1
    # if the first list is empty, return the second list
    if len(lst1) == 0:
        return lst2
    # if the second list is empty, return the first list
    if len(lst2) == 0:
        return lst1
    # if the first list has char less than the second list
    # return the first list
    if len(lst1[0]) < len(lst2[0]):
        return lst1
    # if the second list has char less than the first list
    # return the second list
    return lst2

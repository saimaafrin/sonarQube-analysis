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

    lst1_total_match = 0
    for x in lst1:
        for y in x:
            lst1_total_match += 1

    lst2_total_match = 0
    for x in lst2:
        for y in x:
            lst2_total_match += 1

    if lst1_total_match > lst2_total_match:
        return lst2
    elif lst2_total_match > lst1_total_match:
        return lst1
    else:
        return lst1

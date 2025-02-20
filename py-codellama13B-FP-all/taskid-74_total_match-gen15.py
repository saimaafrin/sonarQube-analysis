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


    if len(lst1) == 0 and len(lst2) == 0:
        return []

    if len(lst1) == 0:
        return lst2

    if len(lst2) == 0:
        return lst1

    total1 = sum([len(s) for s in lst1])
    total2 = sum([len(s) for s in lst2])

    if total1 > total2:
        return lst2
    elif total1 < total2:
        return lst1
    else:
        return lst1

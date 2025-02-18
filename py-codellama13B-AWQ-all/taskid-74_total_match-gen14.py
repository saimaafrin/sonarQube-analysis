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

    total_chars_list_1 = sum(len(x) for x in lst1)
    total_chars_list_2 = sum(len(x) for x in lst2)

    if total_chars_list_1 < total_chars_list_2:
        return lst1
    elif total_chars_list_2 < total_chars_list_1:
        return lst2
    else:
        return lst1

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

    total_lst_len = len(lst1) + len(lst2)
    if len(lst1) == len(lst2):
        return lst1
    elif len(lst1) > len(lst2):
        for i in range(len(lst1)):
            for j in range(len(lst2)):
                if len(lst1[i]) < len(lst2[j]):
                    total_lst_len -= 1
    else:
        for i in range(len(lst2)):
            for j in range(len(lst1)):
                if len(lst2[i]) < len(lst1[j]):
                    total_lst_len -= 1
    if total_lst_len < len(lst1):
        return lst2
    else:
        return lst1

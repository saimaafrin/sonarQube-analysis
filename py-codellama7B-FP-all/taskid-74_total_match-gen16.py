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

    lst_1 = list()
    lst_2 = list()

    if len(lst1) >= len(lst2):
        lst_1 = lst1
        lst_2 = lst2
    else:
        lst_1 = lst2
        lst_2 = lst1

    for i in range(len(lst_1)):
        if len(lst_1[i]) < len(lst_2[i]):
            lst_2.append(lst_1[i])

    return lst_2

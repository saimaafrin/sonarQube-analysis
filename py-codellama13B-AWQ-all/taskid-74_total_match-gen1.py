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

    total_char_list1 = 0
    for word in lst1:
        total_char_list1 += len(word)
    total_char_list2 = 0
    for word in lst2:
        total_char_list2 += len(word)
    
    if total_char_list1 < total_char_list2:
        return lst1
    elif total_char_list1 == total_char_list2:
        return lst1
    else:
        return lst2

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

    lst2 = sorted(lst2, key=lambda x: len(x))
    lst1 = sorted(lst1, key=lambda x: len(x))
    min_length = len(lst1[0])
    ans = []
    for i in range(len(lst1)):
        if min_length < len(lst2[0]):
            return ans
        if len(lst1[i]) <= len(lst2[0]):
            ans.append(lst1[i])
            min_length = len(lst1[i])
    return ans

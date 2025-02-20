from typing import List, Optional

def next_smallest(lst: List[int]) -> Optional[int]:
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    >>> next_smallest([1, 2, 3, 4, 5])
    2
    >>> next_smallest([5, 1, 4, 3, 2])
    2
    >>> next_smallest([])
    None
    >>> next_smallest([1, 1])
    None
    """

    # lst = list(set(lst))  # remove duplicates
    n = len(lst)
    if n < 2:
        return None

    # sort the list
    lst.sort()

    # if the smallest and second smallest are equal, return None
    if lst[0] == lst[1]:
        return None
    else:
        return lst[1]

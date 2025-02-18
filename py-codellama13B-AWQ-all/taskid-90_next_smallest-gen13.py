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

    if len(lst) == 0:
        return None
    # sort the list
    lst.sort()
    # find the smallest element
    smallest = lst[0]
    # loop through the list and find the 2nd smallest
    for i in range(1, len(lst)):
        if lst[i] == smallest:
            continue
        else:
            return lst[i]
    # if the loop finishes without returning, then there is no 2nd smallest
    return None

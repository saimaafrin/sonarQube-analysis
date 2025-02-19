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

    if len(lst) < 2:
        return None

    # sort a copy of the list
    lst_sorted = sorted(lst)

    # find the smallest element
    smallest = lst_sorted[0]
    smallest_index = lst.index(smallest)

    # find the next smallest element
    next_smallest_index = smallest_index + 1
    next_smallest = None

    if next_smallest_index < len(lst):
        next_smallest = lst_sorted[next_smallest_index]

    return next_smallest

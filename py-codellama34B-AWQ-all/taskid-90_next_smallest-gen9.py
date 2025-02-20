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

    if not lst:
        return None
    # sort the list
    lst = sorted(lst)
    # find the first occurence of lst[1] in lst
    for idx, val in enumerate(lst[1:], start=1):
        if val == lst[1]:
            return lst[idx]
    # if we get here, there are no duplicates of lst[1], therefore there is no next smallest
    return None

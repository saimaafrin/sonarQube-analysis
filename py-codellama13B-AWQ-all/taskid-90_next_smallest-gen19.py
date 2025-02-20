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
    # sort the list
    sorted_list = sorted(lst)
    # find the second smallest number
    i = 1
    while i < len(sorted_list) and sorted_list[i] == sorted_list[i-1]:
        i += 1
    if i == len(sorted_list):
        return None
    return sorted_list[i]

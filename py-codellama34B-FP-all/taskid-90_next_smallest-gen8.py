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


    sorted_list = sorted(lst)
    if len(sorted_list) < 2:
        return None

    for i in range(len(sorted_list) - 1):
        if sorted_list[i + 1] > sorted_list[i]:
            return sorted_list[i]

    return None

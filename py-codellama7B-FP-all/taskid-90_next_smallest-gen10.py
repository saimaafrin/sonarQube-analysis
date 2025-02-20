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
    small = small_set = set()
    for i in range(len(lst)):
        if len(small) < 2:
            small.add(lst[i])
        else:
            small_set.add(lst[i])
        if len(small) == len(small_set):
            return None
    return sorted(small_set)[1]

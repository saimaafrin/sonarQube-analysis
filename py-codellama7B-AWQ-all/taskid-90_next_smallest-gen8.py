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

    # Sort the list in ascending order.
    lst.sort()
    # If there are at least 2 elements in the list, return the second element.
    if len(lst) >= 2:
        return lst[1]
    # If there is only 1 element in the list, return None.
    else:
        return None

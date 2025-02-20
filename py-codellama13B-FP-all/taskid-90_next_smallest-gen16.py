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

    # Sort the list
    lst.sort()

    # Find the 2nd smallest
    for i in range(len(lst)):
        # If the next element is greater than the current element, then it is the 2nd smallest
        if i + 1 < len(lst) and lst[i] < lst[i + 1]:
            return lst[i]

    # If no such element is found, then return None
    return None

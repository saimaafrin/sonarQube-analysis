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
    else:
        smallest = lst[0]
        for i in range(1, len(lst)):
            if lst[i] < smallest:
                smallest = lst[i]
        second = lst[0]
        for i in range(1, len(lst)):
            if lst[i] < second and lst[i] != smallest:
                second = lst[i]
        if second == smallest:
            return None
        else:
            return second

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

    smallest = lst[0]
    second_smallest = None
    for i in lst:
        if i < smallest:
            second_smallest = smallest
            smallest = i
        elif second_smallest and second_smallest > i:
            second_smallest = i
    return second_smallest

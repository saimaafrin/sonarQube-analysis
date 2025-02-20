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

    # Find the smallest element
    smallest = None
    for i in range(len(lst)):
        if smallest is None or lst[i] < smallest:
            smallest = lst[i]

    # Find the second smallest element
    second_smallest = None
    for i in range(len(lst)):
        if lst[i] != smallest and (second_smallest is None or lst[i] < second_smallest):
            second_smallest = lst[i]

    return second_smallest

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


    # TODO - your code here
    # Step 1: Find the index of the smallest element
    smallest = min(lst)
    smallest_index = lst.index(smallest)
    # Step 2: Find the index of the next smallest element
    next_smallest_index = (smallest_index + 1) % len(lst)
    # Step 3: Return the next smallest element
    return lst[next_smallest_index]

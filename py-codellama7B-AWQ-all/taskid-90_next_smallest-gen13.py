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

    # your code here
    if len(lst) < 2:
        return None
    second_smallest = None
    for element in lst:
        if second_smallest == None:
            if lst[1] > element:
                second_smallest = element
        else:
            if lst[1] < element < second_smallest:
                second_smallest = element
    return second_smallest

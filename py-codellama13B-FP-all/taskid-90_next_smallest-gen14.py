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

    # Check if the list is empty
    if len(lst) == 0:
        return None
    # Initialize the minimum and second minimum values to the first element
    min1 = min2 = lst[0]
    for i in range(1, len(lst)):
        # If the element is less than the minimum, then it is the second minimum
        if lst[i] < min1:
            min2 = min1
            min1 = lst[i]
        # If the element is less than the second minimum and greater than the minimum, then it is the second minimum
        elif lst[i] < min2:
            min2 = lst[i]
    # Return the second minimum. If the minimum is the only element, then return None
    return min2 if min1 != min2 else None

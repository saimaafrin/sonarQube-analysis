from typing import List

def can_arrange(arr: List[int]) -> int:
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    >>> can_arrange([1, 2, 4, 3, 5])
    3
    >>> can_arrange([1, 2, 3])
    -1
    """

    # Initialize the variables.
    largest_index: int = -1

    for index in range(1, len(arr)):
        if arr[index] < arr[index - 1]:
            if index - 1 > largest_index:
                largest_index = index - 1
        elif index == len(arr) - 1:
            if largest_index == -1:
                return -1
            return largest_index
    
    if largest_index == -1:
        return -1
    return largest_index

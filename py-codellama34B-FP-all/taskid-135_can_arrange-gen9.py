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

    largest_index = -1
    for index, value in enumerate(arr):
        if index > 0 and value >= arr[index - 1]:
            continue
        if value > arr[largest_index]:
            largest_index = index
    return largest_index

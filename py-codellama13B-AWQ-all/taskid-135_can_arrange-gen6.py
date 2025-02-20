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

    # If the array is empty or has only one element, it cannot be rearranged
    if len(arr) < 2:
        return -1

    # Initialize the largest index of an element which is not greater than or
    # equal to the element immediately preceding it to -1
    largest_index = -1

    # Iterate over the elements of the array
    for i in range(1, len(arr)):
        # If the current element is not greater than or equal to the element
        # immediately preceding it, update the largest index of an element
        # which is not greater than or equal to the element immediately
        # preceding it
        if arr[i] < arr[i - 1]:
            largest_index = i

    return largest_index

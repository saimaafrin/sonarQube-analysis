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

    # Initialize variables
    largest_index = -1
    current_largest_value = -1

    # Loop through list and find largest value
    for index, value in enumerate(arr):
        if value > current_largest_value:
            largest_index = index
            current_largest_value = value

    # Check if value at largest_index is greater than the previous value
    if largest_index == 0 or arr[largest_index] <= arr[largest_index - 1]:
        return -1
    return largest_index

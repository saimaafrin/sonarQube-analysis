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

    # Check if the array has only one element
    if len(arr) == 1:
        return -1

    # Initialize the maximum index
    max_index = -1

    # Loop through the array
    for i in range(len(arr) - 1):
        # Check if the current element is less than or equal to the next
        # element
        if arr[i] <= arr[i + 1]:
            # Check if the current element is greater than the element
            # at the maximum index
            if arr[i] > arr[max_index]:
                # Update the maximum index
                max_index = i

    # Return the maximum index
    return max_index

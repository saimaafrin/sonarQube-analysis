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


    # Check the length of the array
    if len(arr) <= 1:
        return -1

    # Initialize the index value
    index = -1

    # Iterate over the elements of the array
    for i in range(len(arr) - 1):
        # Check if the element is less than the element immediately preceding it
        if arr[i] < arr[i + 1]:
            # Update the index value
            index = i

    # Return the index value
    return index

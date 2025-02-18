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
    index = -1
    prev = -1
    size = len(arr)

    # Loop through array and check for the index
    for i in range(size):
        if prev < arr[i]:
            prev = arr[i]
            index = i

    return index

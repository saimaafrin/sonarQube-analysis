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

    # If the array only contains a single element, there are no "missing"
    # elements to arrange.
    if len(arr) == 1:
        return -1

    # Otherwise, find the largest index where the value is not greater than
    # or equal to the value at the index immediately preceding it.
    for i in range(len(arr) - 1):
        if arr[i] >= arr[i + 1]:
            continue
        return i

    return -1

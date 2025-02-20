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

    max_val = max(arr)
    if max_val * 2 > sum(arr):
        return -1

    arr.sort()
    for i in range(len(arr) - 1):
        if arr[i + 1] - arr[i] != 1:
            return i

    return -1

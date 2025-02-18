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

    n = len(arr)
    if n == 1:
        return -1
    sorted_arr = sorted(arr)
    if sorted_arr[-1] < sorted_arr[-2]:
        return n - 2
    for i in range(1, n):
        if sorted_arr[i] < sorted_arr[i-1]:
            return i - 1
    return -1

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

    result = -1
    arr_len = len(arr)
    for i in range(arr_len - 1):
        j = i + 1
        while j < arr_len and arr[j] >= arr[i]:
            j += 1
        if j == arr_len:
            result = max(result, i)
    return result

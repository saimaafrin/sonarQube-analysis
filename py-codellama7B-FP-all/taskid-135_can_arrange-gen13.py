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
    if n <= 1:
        return -1

    # The largest index of an element which is not greater than or equal to
    # the element immediately preceding it.
    largest_index = -1

    for i in range(n - 1):
        if arr[i] <= arr[i + 1]:
            continue

        largest_index = i

    return largest_index

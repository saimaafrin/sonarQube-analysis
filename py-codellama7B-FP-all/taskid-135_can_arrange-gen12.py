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


    # Base case, the array is length 1 or less, which means it is already
    # in descending order.
    if len(arr) <= 1:
        return -1

    # We assume that the array is not in descending order.
    largest_index = -1

    for i in range(len(arr) - 1):
        if arr[i] <= arr[i + 1]:
            continue
        largest_index = i
        break

    # If the largest element is found then we know the array is in descending
    # order.
    return largest_index if largest_index == -1 else -1

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

    # Find the sum of the array
    total = sum(arr)

    # Check if the sum is even
    if total % 2 == 1:
        return -1

    # Check if all the elements are positive
    if all(x > 0 for x in arr):
        return -1

    # Check if all the elements are negative
    if all(x < 0 for x in arr):
        return -1

    # Find the largest index of an element which is not
    # greater than or equal to the element immediately preceding it
    max_index = -1
    for i in range(len(arr)):
        if arr[i] > arr[i-1]:
            max_index = i

    return max_index

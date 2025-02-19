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

    if not arr:
        return -1

    # check the first element is the smallest
    if arr[0] < min(arr[1:], default=arr[0]):
        return -1

    # check the last element is the largest
    if max(arr[:-1], default=arr[-1]) < arr[-1]:
        return -1

    # find the largest index of an element
    # which is not greater than or equal to
    # the element immediately preceding it
    for i in range(len(arr) - 1):
        if arr[i + 1] < arr[i]:
            return i

    # all the elements are in the right order
    return len(arr) - 1

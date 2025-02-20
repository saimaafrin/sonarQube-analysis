from typing import List

def smallest_change(arr: List[int]) -> int:
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    >>> smallest_change([1, 2, 3, 5, 4, 7, 9, 6])
    4
    >>> smallest_change([1, 2, 3, 4, 3, 2, 2])
    1
    >>> smallest_change([1, 2, 3, 2, 1])
    0
    """

    # The number of changes required is the minimum number of elements
    # that needs to be changed to make the array palindromic.
    # The number of elements in the array is the length of the array.
    return min(len(arr), sum(1 for i in range(len(arr) // 2 + 1) if arr[i] != arr[~i]))

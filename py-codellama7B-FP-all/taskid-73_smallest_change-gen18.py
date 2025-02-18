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

    # Sort the array in ascending order
    arr.sort()
    # If the first and last elements are not equal, then return the absolute difference between them
    if arr[0] != arr[-1]:
        return abs(arr[0] - arr[-1])
    # Else, if the array is already palindromic, then return 0
    else:
        return 0

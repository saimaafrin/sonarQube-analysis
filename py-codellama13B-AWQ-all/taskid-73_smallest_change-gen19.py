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

    if len(arr) < 2:
        return 0

    # Check if the array is already a palindrome
    if arr == arr[::-1]:
        return 0

    # Get the middle of the array
    mid = len(arr) // 2

    # Count the number of differences
    diff = 0
    for i in range(mid):
        if arr[i] != arr[~i]:
            diff += 1

    # If the array is not a palindrome, then return the number of differences
    return diff

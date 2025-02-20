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

    # If array is already palindromic return 0
    if is_palindromic(arr):
        return 0

    # If the first and last elements are equal, we can change all the
    # other elements to get a palindromic array
    if arr[0] == arr[-1]:
        return len(arr) - 1

    # Find the first and last elements that are not equal
    first_idx = find_idx(arr, 0)
    last_idx = find_idx(arr, -1)

    # If we can change all the elements between first and last indices
    # to get a palindromic array, then we need to change only the first and last indices
    if first_idx > last_idx:
        return 2

    # Otherwise, we need to change all the elements between first and last indices
    # and first and last indices
    return last_idx - first_idx + 2

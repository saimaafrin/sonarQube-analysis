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

    if len(arr) == 0:
        return 0

    # check if the array is already palindromic
    if arr == arr[::-1]:
        return 0

    # find the middle of the array
    mid = len(arr) // 2

    # check if the first half of the array is palindromic
    if arr[mid:] == arr[mid:][::-1]:
        return mid

    # check if the second half of the array is palindromic
    if arr[:mid] == arr[:mid][::-1]:
        return len(arr) - mid

    # if both the first and second halves of the array are not palindromic,
    # then find the minimum number of elements needed to be changed
    # to make the array palindromic
    for i in range(mid):
        if arr[i] != arr[len(arr) - 1 - i]:
            return 2

    return 0

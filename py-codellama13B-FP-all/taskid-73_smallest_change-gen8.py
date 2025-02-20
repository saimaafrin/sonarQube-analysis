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

    arr.sort()
    left, right = 0, len(arr) - 1
    count = 0
    while left < right:
        if arr[left] != arr[right]:
            count += 1
            arr[left] = arr[right]
            left += 1
        else:
            left += 1
            right -= 1
    return count

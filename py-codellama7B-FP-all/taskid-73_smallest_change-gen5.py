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

    arr_sorted = sorted(arr)
    n = len(arr_sorted)
    left = 0
    right = n - 1
    count = 0
    while left < right:
        if arr_sorted[left] == arr_sorted[right]:
            left += 1
            right -= 1
        else:
            count += 1
            if arr_sorted[left] == arr_sorted[right] - 1:
                left += 1
            else:
                right -= 1
    return count

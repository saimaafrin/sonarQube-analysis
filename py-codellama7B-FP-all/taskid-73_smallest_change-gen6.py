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

    n = len(arr)
    left = [0] * n
    right = [0] * n

    left[-1] = arr[0]
    for i in range(n-2, -1, -1):
        left[i] = min(left[i+1], arr[i])

    right[0] = arr[-1]
    for i in range(1, n):
        right[i] = min(right[i-1], arr[n-i-1])

    count = 0
    for i in range(n):
        if arr[i] != left[i] and arr[i] != right[i]:
            count += 1

    return count

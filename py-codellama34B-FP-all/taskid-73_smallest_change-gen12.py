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
    if n == 1:
        return 0
    mid = n // 2
    if n % 2:
        for i in range(n // 2, n):
            if arr[i] != arr[mid]:
                arr[i] = arr[mid]
                mid -= 1
    else:
        for i in range(n // 2 - 1, -1, -1):
            if arr[i] != arr[mid]:
                arr[i] = arr[mid]
                mid += 1
    return n // 2 - mid

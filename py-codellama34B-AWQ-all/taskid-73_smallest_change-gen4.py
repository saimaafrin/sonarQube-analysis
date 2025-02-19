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

    def is_palindromic(arr: List[int], start: int, end: int) -> bool:
        while start <= end:
            if arr[start] != arr[end]:
                return False
            start += 1
            end -= 1
        return True

    n = len(arr)
    if n == 1 or is_palindromic(arr, 0, n - 1):
        return 0

    res = n
    for i in range(n):
        j = n - 1 - i
        if arr[i] != arr[j]:
            res = min(res, 1 + smallest_change(arr[:i] + arr[i+1:j] + arr[j+1:]))
    return res

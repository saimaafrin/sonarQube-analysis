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
    if n == 0:
        return 0
    dp = [[-1 for i in range(n+1)] for j in range(n+1)]
    dp[0][0] = 0
    return min(smallest_change_util(arr, 0, n-1, dp), smallest_change_util(arr, 1, n, dp))

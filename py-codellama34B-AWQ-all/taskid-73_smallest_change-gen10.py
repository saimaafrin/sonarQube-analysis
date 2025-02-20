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
    # initialize dp array
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for i in range(n - 1):
        dp[i][i + 1] = 1 if arr[i] == arr[i + 1] else 0
    for i in range(2, n):
        for j in range(0, n - i):
            dp[j][j + i] = dp[j + 1][j + i - 1] if arr[j] == arr[j + i] else max(dp[j][j + i - 1], dp[j + 1][j + i])
    return n - dp[0][n - 1]

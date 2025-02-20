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
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for i in range(1, n):
        if arr[i] == arr[i - 1]:
            dp[i - 1][i] = 1
    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            dp[i][j] = (arr[i] == arr[j] and dp[i + 1][j - 1]) or (dp[i + 1][j] and dp[i][j - 1])
    return (n * (n + 1)) // 2 - sum(sum(x) for x in dp)

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
    dp = [[0] * (n+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(n):
            if i == j:
                dp[i+1][j+1] = dp[i][j]
            else:
                if arr[i] == arr[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = 1 + dp[i][j]
    return dp[n][n]

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
    dp = [[0]*n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0

    # for length 2
    for i in range(n-1):
        if arr[i] == arr[i+1]:
            dp[i][i+1] = 0
        else:
            dp[i][i+1] = 1

    # for length 3 to n
    for k in range(2, n):
        for i in range(n-k):
            j = i + k
            if arr[i] == arr[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1], dp[i+1][j], dp[i+1][j-1])

    return dp[0][n-1]

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
    if n < 2:
        return 0

    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0

    for i in range(n - 1):
        if arr[i] == arr[i + 1]:
            dp[i][i + 1] = 0
        else:
            dp[i][i + 1] = 1

    for i in range(n - 3, -1, -1):
        for j in range(i + 2, n):
            if arr[i] == arr[j] and dp[i + 1][j - 1] == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = 1

    return min([max(dp[i]) for i in range(n)])

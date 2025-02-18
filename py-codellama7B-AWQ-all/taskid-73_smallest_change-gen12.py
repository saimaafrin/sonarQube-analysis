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

    # Time complexity: O(N)
    # Space complexity: O(N)
    n = len(arr)
    # dp[i][j]: min num of changes to make arr[i:j] palindromic
    # dp[i][j] = min(dp[i][j-1], dp[i+1][j], dp[i][j-1] + 1)
    dp = [[inf] * n for _ in range(n)]
    # 0 changes, arr[i:i] is already palindromic
    for i in range(n):
        dp[i][i] = 0
    # i = 0, j = 1
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = min(dp[i][j - 1], dp[i + 1][j], dp[i][j - 1] + 1)

    return dp[0][n - 1]

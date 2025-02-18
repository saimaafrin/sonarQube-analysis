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


    l = len(arr)
    dp = [[0 for i in range(l)] for j in range(l)]

    for i in range(l):
        dp[i][i] = 0

    for i in range(l-1, -1, -1):
        for j in range(i+1, l):
            if arr[i] == arr[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1], dp[i+1][j], dp[i+1][j-1])

    return dp[0][l-1]

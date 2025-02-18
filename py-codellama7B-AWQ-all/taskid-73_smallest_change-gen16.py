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
    # dp[i][j] represents the minimum number of elements to change to make arr[:i+1] a palindromic sequence
    # dp[i][j] = min(dp[i-1][k]+1, where k is an index that arr[:i] is a palindrome)
    dp = [[0] * n for _ in range(n)]
    # palindrome[i][j] represents the index of the middle element of the palindrome arr[:i]
    palindrome = [[0] * n for _ in range(n)]
    for i in range(n):
        palindrome[i][i] = i

    for i in range(n):
        for j in range(i+1, n):
            # if arr[i] == arr[j], dp[i][j] = dp[i-1][j+1]
            if arr[i] == arr[j]:
                dp[i][j] = dp[i-1][j+1]
                palindrome[i][j] = palindrome[i-1][j+1]
            # if arr[i] != arr[j], dp[i][j] = dp[i-1][k] + 1, where k is an index that arr[:i] is a palindrome
            else:
                min_change = 100000000
                for k in range(j, i-1, -1):
                    min_change = min(min_change, dp[i-1][k]+1)
                dp[i][j] = min_change
                palindrome[i][j] = palindrome[i-1][k]

    return dp[n-1][n-1]

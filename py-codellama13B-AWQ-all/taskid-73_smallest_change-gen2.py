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

    # TODO: Check for input list validity
    n = len(arr)

    # Create a matrix for storing the dp values
    dp = [[0] * n for _ in range(n)]

    # Fill the dp table
    for i in range(n):
        for j in range(n):
            # If i==j, then no operations needed as the array is already a palindrome
            if i == j:
                dp[i][j] = 0
            # If i is the last index and j is one position before it,
            # then only one operation needed as we need to flip the first and last elements
            elif i == j-1:
                dp[i][j] = 1
            # If i is one position before j,
            # then we need to flip the first and last elements and the middle elements
            elif i == j-2:
                dp[i][j] = 2
            # If all the above conditions fail,
            # then we need to check if the first and last elements are the same,
            # if they are, then we just need to flip the middle elements
            else:
                dp[i][j] = dp[i+1][j-1]

    # Return the minimum number of operations needed
    return min(dp[0][n-1], dp[1][n-2], dp[2][n-3])

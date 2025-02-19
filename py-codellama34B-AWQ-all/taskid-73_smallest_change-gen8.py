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
    if n <= 1: return 0
    memo = [[0] * n for _ in range(n)]

    def _smallest_change(i: int, j: int) -> int:
        if memo[i][j] != 0:
            return memo[i][j]
        if i == j:
            memo[i][j] = 0
        elif arr[i] == arr[j]:
            memo[i][j] = _smallest_change(i + 1, j - 1)
        else:
            memo[i][j] = 1 + min(
                _smallest_change(i + 1, j),
                _smallest_change(i, j - 1),
            )
        return memo[i][j]

    return _smallest_change(0, n - 1)

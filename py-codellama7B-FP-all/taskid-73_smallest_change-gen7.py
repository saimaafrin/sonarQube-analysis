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
    left = [0] * n
    right = [0] * n

    # Set the left pointer
    for i in range(n):
        left[i] = i

    # Set the right pointer
    for i in range(n - 1, -1, -1):
        right[i] = n - 1 - i

    # Create a map
    # {(i, j): 0} if it is palindromic
    # {(i, j): 1} if it is not palindromic
    palindromic_map = {}

    for i in range(n):
        for j in range(i, n):
            if arr[i] == arr[j]:
                palindromic_map[(i, j)] = 0
            else:
                palindromic_map[(i, j)] = 1

    # Find the smallest change
    min_change = float('inf')

    for i in range(n):
        for j in range(i, n):
            if palindromic_map[(i, j)] == 0:
                continue

            min_change = min(min_change, abs(left[i] - right[j]))

    return min_change

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

    # Solution 1: Naive approach
    # Time complexity: O(N^2)
    # Space complexity: O(1)
    if not arr:
        return 0

    # get the length of the array
    N = len(arr)

    # check if the array is already palindromic
    if is_palindromic(arr):
        return 0

    # the minimum number of changes required
    min_changes = N + 1

    # loop through the array to find the minimum number of changes
    for i in range(N):
        for j in range(i, N):
            # get the range of the array from i to j
            start, end = i, j
            # check if the array in the range is palindromic
            if is_palindromic(arr[start:end]):
                # the minimum number of changes is the range
                min_changes = min(min_changes, end - start + 1)
                break

    return min_changes

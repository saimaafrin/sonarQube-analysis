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

    # Find length of the smallest subarray
    # that needs to be changed
    # to make the array palindromic.
    i, j = 0, n - 1
    count = 0
    while i < j:
        if arr[i] != arr[j]:
            count += 1
        i += 1
        j -= 1

    # Check for odd length palindrome
    # even length palindrome.
    if i == j:
        count = 0 if count % 2 == 0 else 1
    else:
        count = 1 if count % 2 == 0 else 0

    # Check for boundary conditions.
    if count > n // 2:
        count = n - count

    return count

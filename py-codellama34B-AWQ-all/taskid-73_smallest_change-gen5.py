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

    # check if the array is already a palindrome
    is_palindrome = True
    for i in range(len(arr)):
        if arr[i] != arr[len(arr)-i-1]:
            is_palindrome = False
            break

    if is_palindrome:
        return 0

    # compute the size of the longest palindromic subsequence
    # we will need the subsequence to be palindromic, and not just the array
    longest_palindromic_subsequence = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] == arr[j]:
                longest_palindromic_subsequence = max(longest_palindromic_subsequence, j - i + 1)

    return len(arr) - longest_palindromic_subsequence

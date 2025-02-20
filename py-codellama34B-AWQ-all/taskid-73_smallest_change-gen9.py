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
    if n == 1:
        return 0
    if n == 2:
        return 1

    # Compute the longest common prefix between the two arrays
    lcp = 0
    for i in range(n):
        if arr[i] == arr[n - i - 1]:
            lcp += 1
        else:
            break

    # Compute the length of the suffix after the longest common prefix
    suffix = n - 1 - lcp
    # If the suffix is a palindrome, then the answer is the length of the prefix
    if lcp != 0 and suffix == reverse_int(lcp):
        return n - lcp
    # Otherwise, the answer is the length of the array
    else:
        return n

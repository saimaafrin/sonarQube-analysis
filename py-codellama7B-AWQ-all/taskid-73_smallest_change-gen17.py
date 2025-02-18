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
    max_val = max(arr)
    palindromic = [False] * (max_val + 1)

    for i in range(n):
        if arr[i] in palindromic:
            return 0

        # check if the array is palindromic
        for j in range(i + 1, n):
            if arr[j] == arr[i]:
                palindromic[arr[i]] = True
                break

    ans = 0
    for i in range(1, max_val + 1):
        if not palindromic[i]:
            ans += 1

    return ans

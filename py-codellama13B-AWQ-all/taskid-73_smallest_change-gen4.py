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

    length = len(arr)

    # If arr is already a palindrome, then return 0
    if arr == arr[::-1]:
        return 0

    # Find the minimum number of elements to change
    min_changes = length
    for i in range(length // 2):
        if arr[i] != arr[-i - 1]:
            min_changes = min(min_changes, 2)
        else:
            min_changes -= 1

    return min_changes

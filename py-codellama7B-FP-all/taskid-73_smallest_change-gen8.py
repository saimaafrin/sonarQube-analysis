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


    # Solution:
    # 1. Find the middle index of the array.
    # 2. Check if the array is already palindromic.
    # 3. If it's not, we have to change elements on both sides of the middle element.
    # 4. Return the number of changes needed to make the array palindromic.

    mid_idx = len(arr) // 2
    right_idx = mid_idx - 1
    left_idx = mid_idx - 1
    changes = 0

    while right_idx >= 0 and left_idx < len(arr):
        if arr[right_idx] == arr[left_idx]:
            right_idx -= 1
            left_idx += 1
        else:
            changes += 1
            right_idx -= 1
            left_idx += 1

    while left_idx < len(arr):
        changes += 1
        left_idx += 1

    while right_idx >= 0:
        changes += 1
        right_idx -= 1

    return changes

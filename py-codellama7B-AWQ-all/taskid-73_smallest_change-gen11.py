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

    # Start by finding the middle of the array.
    middle = len(arr) // 2

    # Traverse the array from both the left and right sides.
    left = 0
    right = len(arr) - 1
    changes = 0

    while left < middle and right > middle:
        # If the left and right elements don't match, increment the number of changes.
        if arr[left] != arr[right]:
            changes += 1

        left += 1
        right -= 1

    return changes

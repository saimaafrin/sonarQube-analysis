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


    # Check for the simple cases
    if len(arr) == 1:
        return 0
    elif len(arr) == 2:
        if arr[0] == arr[1]:
            return 0
        else:
            return 1

    # Calculate the mid point of the array
    mid = len(arr) // 2

    # Calculate the left and right counts
    left_count = 0
    right_count = 0
    for i in range(mid):
        if arr[i] != arr[len(arr) - i - 1]:
            left_count += 1
        if arr[i] != arr[len(arr) - i - 1]:
            right_count += 1

    # Calculate the minimum changes
    min_left_changes = left_count // 2
    min_right_changes = right_count // 2
    min_changes = min_left_changes + min_right_changes

    return min_changes

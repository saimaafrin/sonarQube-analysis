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


    # Step 1: Check if the array is already palindromic
    is_palindromic = True
    for i in range(0, len(arr) // 2):
        if arr[i] != arr[len(arr) - 1 - i]:
            is_palindromic = False
            break
    if is_palindromic:
        return 0

    # Step 2: If the array is not palindromic, find the minimum number of elements
    # that need to be changed.
    i, j = 0, len(arr) - 1
    changes = 0
    while i < j:
        if arr[i] != arr[j]:
            changes += 1
        i += 1
        j -= 1

    return changes

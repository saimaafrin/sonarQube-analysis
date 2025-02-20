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

    arr_len = len(arr)
    if arr_len == 0:
        return 0

    max_val = max(arr)
    if max_val == 0:
        return 0

    right_index = arr_len - 1
    left_index = 0

    min_changes = 0
    while right_index > left_index:
        right_val = arr[right_index]
        left_val = arr[left_index]

        if right_val > left_val:
            min_changes += 1

        if right_val == left_val:
            right_index -= 1
            left_index += 1
        else:
            right_index -= 1
            left_index += 1

    if arr[right_index] != arr[left_index]:
        min_changes += 1

    return min_changes

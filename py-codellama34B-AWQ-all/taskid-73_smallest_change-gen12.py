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
    if arr_len < 2:
        return 0

    # We only need to check up to half of the array
    # Because the second half of the array is a reversed version of the first half
    arr_mid = arr_len // 2
    arr_range = range(arr_mid + 1)
    min_changes = arr_len
    for i in arr_range:
        left, right = arr[:arr_mid - i], arr[arr_mid + i :]
        if left == right[::-1]:
            min_changes = min(min_changes, 2 * i)
        elif i > 0:
            min_changes = min(min_changes, 2 * (i - 1) + 1)
    return min_changes

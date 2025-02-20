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
    if arr_len == 1:
        return 0

    arr_first = arr[:arr_len//2]
    arr_last = arr[arr_len//2:]
    arr_last.reverse()

    if arr_first == arr_last:
        return 0
    else:
        return 1 + smallest_change(arr_first[:-1] + arr_first[1:])

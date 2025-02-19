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

    # check if array is already palindrome
    # for i in range(arr_len // 2):
    #     if arr[i] != arr[arr_len - 1 - i]:
    #         break
    # else:
    #     return 0

    # create a new array which is the reverse of the given array
    arr_rev = arr[::-1]
    i, j = 0, 0
    changed = 0

    # find number of elements that need to be changed
    while i < arr_len:
        if arr[i] != arr_rev[j]:
            changed += 1
        i += 1
        j += 1

    return changed

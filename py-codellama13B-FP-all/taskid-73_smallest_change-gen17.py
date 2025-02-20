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


    arr.sort()
    i = 0
    while arr[i] == i+1:
        i += 1
    if i == len(arr)-1:
        return 0
    j = len(arr)-1
    while arr[j] == j+1:
        j -= 1
    return min(len(arr)-i-j, i+j-len(arr)+1)

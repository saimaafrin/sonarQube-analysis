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

    # reverse of the array
    rev = arr[::-1]

    # loop until one array is empty
    while arr and rev:
        if arr[0] == rev[0]:
            arr.pop(0)
            rev.pop(0)
        else:
            arr.pop(0)
            arr.append(rev.pop(0))

    # count the number of elements in both arrays
    return len(arr) + len(rev)

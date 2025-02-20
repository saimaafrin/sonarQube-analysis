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

    n = len(arr)
    is_palindromic = [False] * n
    for i in range(n):
        if i == 0:
            is_palindromic[0] = True
        else:
            if arr[i] == arr[i-1]:
                is_palindromic[i] = is_palindromic[i-1]
            else:
                is_palindromic[i] = True
    if is_palindromic[-1] == True:
        return 0
    else:
        for i in range(n):
            if is_palindromic[i] == False:
                return n - i
    return n

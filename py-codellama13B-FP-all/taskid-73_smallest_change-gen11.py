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


    def is_palindrome(arr: List[int]) -> bool:
        return arr == arr[::-1]

    if is_palindrome(arr):
        return 0

    for i in range(len(arr)):
        if arr[i] != arr[len(arr) - i - 1]:
            break
    else:
        return 0

    # change all elements on the left side to be the same as the element on the right side
    for i in range(i):
        arr[i] = arr[len(arr) - i - 1]

    # change all elements on the right side to be the same as the element on the left side
    for i in range(len(arr) - i):
        arr[len(arr) - i - 1] = arr[i]

    return i + 1

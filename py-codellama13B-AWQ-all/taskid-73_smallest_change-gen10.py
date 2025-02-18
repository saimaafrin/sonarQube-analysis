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

    # If the array is already palindromic, return 0
    if is_palindrome(arr):
        return 0

    # Find the middle of the array
    middle = len(arr) // 2

    # Find the first and last indices of the array that are not equal
    # and return the number of elements that need to be changed
    for i in range(middle):
        if arr[i] != arr[len(arr) - i - 1]:
            return len(arr) - i - 1

    return len(arr)

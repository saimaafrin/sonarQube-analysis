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

    # check if arr is a palindrome and return 0
    if arr == arr[::-1]:
        return 0

    # check if arr is a palindrome with the first and last elements swapped and return 1
    if arr == arr[::-1][1:-1]:
        return 1

    # initialize a variable to keep track of the minimum number of elements that need to be changed
    # to make the array palindromic
    min_changes = float('inf')

    # loop through each element in the array
    for i in range(len(arr)):
        # check if the element is a palindrome with the first and last elements swapped
        # and return the number of changes needed to make the array palindromic
        if arr[i:] == arr[i:][::-1]:
            return len(arr) - i - 1

    # return the minimum number of elements that need to be changed to make the array palindromic
    return min_changes

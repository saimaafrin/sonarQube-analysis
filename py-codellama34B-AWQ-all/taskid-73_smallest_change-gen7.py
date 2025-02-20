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

    # Check if length is less than 2
    if len(arr) < 2:
        return 0

    # Get the midpoint of the array
    mid = len(arr) // 2

    # Get the left and right slices of the array
    left = arr[:mid]
    right = arr[mid:]

    # Check if the length of the array is odd
    if len(arr) % 2:
        right = right[1:]

    # Check if the length of the slices are the same
    if len(left) != len(right):
        right = right[:-1]

    # Reverse the right slice
    right.reverse()

    # Get the number of elements that need to be changed
    diff = sum([i != j for i, j in zip(left, right)])

    return diff

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

    # edge case - empty array
    if not arr:
        return 0

    # edge case - single element
    if len(arr) == 1:
        return 0

    # edge case - two elements
    if len(arr) == 2:
        return arr[0] == arr[1]

    # initialize result variable and loop variables
    result = 0
    left_index = 0
    right_index = len(arr) - 1

    # loop through array
    while left_index < right_index:
        # if elements are not equal, increment result
        if arr[left_index] != arr[right_index]:
            result += 1

        # increment left_index and right_index
        left_index += 1
        right_index -= 1

    # if elements are not equal, increment result
    if arr[0] != arr[len(arr) - 1]:
        result += 1

    return result

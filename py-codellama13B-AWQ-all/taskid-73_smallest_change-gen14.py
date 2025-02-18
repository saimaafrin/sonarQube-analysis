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


    # if arr is empty return 0
    if len(arr) == 0:
        return 0

    # if arr is of size 1 return 0
    if len(arr) == 1:
        return 0

    # initialize left, right, and count variables
    left = 0
    right = len(arr) - 1
    count = 0

    # check if the array is already palindromic
    while left <= right:
        # check if the element at left index is not the same as right index
        if arr[left] != arr[right]:
            # increment the count and swap the elements
            count += 1
            arr[left], arr[right] = arr[right], arr[left]

        # move on to the next index
        left += 1
        right -= 1

    # return the count
    return count

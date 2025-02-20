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

    # initialize variables
    size = len(arr)
    left, right = 0, size-1
    count = 0

    # find the middle index
    mid = size // 2

    # compare the left and right index of the array
    while left < right:
        if arr[left] != arr[right]:
            if arr[left] < arr[right]:
                # if left is smaller than right, the left index gets incremented
                # and the count gets incremented
                arr[left] += 1
                count += 1
            else:
                # if left is larger than right, the right index gets decremented
                # and the count gets incremented
                arr[right] -= 1
                count += 1
        # increment both indices
        left += 1
        right -= 1
    # if the middle index is less than the left index
    if mid < left:
        count += 1
    # return the count
    return count

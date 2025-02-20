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

    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] == arr[right]:
            left += 1
            right -= 1
        else:
            return 1

    if left == right:
        return 0

    count = 0

    # Check if the middle elements are the same
    for i in range(left + 1, right):
        if arr[left] != arr[i]:
            count += 1

    return count

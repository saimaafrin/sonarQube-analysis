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

    # O(n) time and O(n) space
    n = len(arr)
    # if the array is already palindromic return 0
    if is_palindromic(arr):
        return 0
    # if the array has only one element return 1
    if n == 1:
        return 1
    # if the array has two elements, check if they are equal
    if n == 2:
        if arr[0] != arr[1]:
            return 1
        return 0
    # initialize the minimum number of changes to change
    min_changes = n
    # loop through the array
    for i in range(n):
        # if the element at index i is equal to the element at index n - 1 - i
        if arr[i] == arr[n - 1 - i]:
            # set the minimum number of changes to the number of elements in the array
            min_changes = n
            # break the loop
            break
        # if the element at index i is not equal to the element at index n - 1 - i
        else:
            # set the minimum number of changes to the minimum of the current number of
            # changes and the difference between the index of the element and the index
            # of the element that is equal to the element at index i
            min_changes = min(min_changes, abs(i - (n - 1 - arr[i])))
    # return the minimum number of changes
    return min_changes

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

    # convert the array to a palindrome first
    arr = get_palindrome(arr)
    # get the length of the palindrome
    palindrome_length = len(arr)
    # init the changes to zero
    changes = 0
    # loop over the palindrome
    for i in range(0, palindrome_length):
        # check if the current element is not the same as the previous element
        if arr[i] != arr[i - 1]:
            # increment the number of changes
            changes += 1
    # return the number of changes
    return changes

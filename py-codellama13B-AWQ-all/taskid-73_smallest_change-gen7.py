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

    # Edge case: Empty list
    if not arr:
        return 0

    # Initialize min changes
    min_changes = 0

    # Initialize left and right indices
    left, right = 0, len(arr) - 1

    # Check if array is already palindromic
    if left == right:
        return 0

    # Iterate through the list
    while left <= right:
        # If the current elements are different, we need to change one of them
        if arr[left] != arr[right]:
            min_changes += 1
            # Check if left and right elements need to be changed
            if abs(arr[left] - arr[right]) > 1:
                min_changes += 1

        # Increment left and right indices
        left += 1
        right -= 1

    # Return the min changes
    return min_changes

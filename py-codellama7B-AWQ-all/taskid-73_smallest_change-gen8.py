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

    # Initialize left and right pointers at the beginning and end of the array
    left, right = 0, len(arr) - 1
    # Initialize a variable to store the minimum number of elements that need to be changed
    min_changes = float('inf')

    # While the left pointer is before the right pointer
    while left < right:
        # If the element at the left pointer is the same as the element at the right pointer
        if arr[left] == arr[right]:
            # Increment the left and right pointers
            left += 1
            right -= 1
        # Otherwise
        else:
            # If the left pointer is before the right pointer
            if left < right:
                # Set the minimum number of elements that need to be changed to the minimum of
                # the current minimum and the number of elements between the left and right pointers
                min_changes = min(min_changes, right - left)

                # Increment the right pointer
                right -= 1
            # Otherwise
            else:
                # Set the minimum number of elements that need to be changed to the minimum of
                # the current minimum and the number of elements between the left and right pointers
                min_changes = min(min_changes, left - right)

                # Increment the left pointer
                left += 1

    # Return the minimum number of elements that need to be changed
    return min_changes

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


    # This solution works by keeping track of the number of changes needed
    # to make the array palindromic, and the number of elements in the array
    # that have already been changed.

    # For example, if we have the array:
    # [1, 2, 3, 5, 4, 7, 9, 6]

    # We can make the first three elements palindromic by changing the first 3
    # elements to: [3, 2, 1]
    # This array is now palindromic, and we have made a total of 3 changes.

    # We can then make the second half of the array palindromic by changing
    # the next 3 elements to: [4, 4, 4]
    # This array is now palindromic, and we have made a total of 6 changes.

    # We can then make the final element palindromic by changing it to 4.
    # This array is now palindromic, and we have made a total of 7 changes.

    # This solution is O(N) time and O(1) space.

    n = len(arr)
    if n == 1:
        return 0

    # This keeps track of the number of elements that have been changed.
    changes = 0

    # This keeps track of the number of elements that need to be changed.
    remaining = n // 2

    # This keeps track of the number of elements that need to be changed
    # in order to make the array palindromic.
    minimum = n

    # We iterate from the start and end of the array, and compare the
    # elements at each index.
    for i in range(n // 2):
        # If the elements at each index are not equal, then we
        # need to change one of the elements.
        if arr[i] != arr[n - 1 - i]:
            # If we have already made the maximum number of changes,
            # then we can return the number of changes that we have made.
            if changes == remaining:
                return minimum

            # Otherwise, we need to increment the number of changes
            # that we have made.
            changes += 1

            # If the element at the current index is greater than
            # the element at the opposite index, then we change the
            # element at the current index to match the element at
            # the opposite index.
            if arr[i] > arr[n - 1 - i]:
                arr[i] = arr[n - 1 - i]
            # If the element at the current index is less than
            # the element at the opposite index, then we change the
            # element at the opposite index to match the element at
            # the current index.
            elif arr[i] < arr[n - 1 - i]:
                arr[n - 1 - i] = arr[i]

    # If we have made the maximum number of changes,
    # then we can return the number of changes that we have made.
    if changes == remaining:
        return minimum

    # Otherwise, we need to increment the number of changes
    # that we have made.
    changes += 1

    # We then iterate from the start and end of the array, and compare
    # the elements at each index.
    for i in range(n // 2):
        # If the elements at each index are not equal, then we
        # need to change one of the elements.
        if arr[i] != arr[n - 1 - i

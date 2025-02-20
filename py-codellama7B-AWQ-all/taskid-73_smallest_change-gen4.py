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

    # Find the first element to be changed
    first_change = find_first_change(arr)
    # Find the last element to be changed
    last_change = find_last_change(arr)

    # If the elements are already palindromic, just return 0
    if not first_change and not last_change:
        return 0

    # If the first element is to be changed
    if first_change:
        # If the last element is to be changed
        if last_change:
            # Both elements need to be changed
            return 2
        # The last element doesn't need to be changed
        else:
            # The first element needs to be changed
            return 1
    # The first element doesn't need to be changed
    else:
        # If the last element is to be changed
        if last_change:
            # The first element needs to be changed
            return 1
        # Both elements don't need to be changed
        else:
            return 0

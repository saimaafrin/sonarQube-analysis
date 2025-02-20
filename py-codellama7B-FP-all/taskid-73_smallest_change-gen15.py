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


    # Solution: O(n log n) time | O(n) space
    # This solution is based on the idea of finding the first and the last
    # non-equal elements of the array, and then changing them.

    # Find the first and the last non-equal elements of the array
    first_non_equal_index = None
    last_non_equal_index = None
    for i in range(len(arr)):
        for j in range(len(arr) - 1, i, -1):
            if arr[i] != arr[j]:
                if first_non_equal_index is None:
                    first_non_equal_index = i
                last_non_equal_index = j
                break

    # If there are no non-equal elements in the array,
    # then the array is already palindromic
    if first_non_equal_index is None:
        return 0

    # If the first non-equal element is located on the leftmost side of the array
    # and the last non-equal element is located on the rightmost side of the array,
    # then we can change only these elements
    if first_non_equal_index == 0 and last_non_equal_index == len(arr) - 1:
        return 2

    # If the first non-equal element is located on the rightmost side of the array
    # and the last non-equal element is located on the leftmost side of the array,
    # then we can change only these elements
    if first_non_equal_index == len(arr) - 1 and last_non_equal_index == 0:
        return 2

    # If the first non-equal element is located on the rightmost side of the array
    # and the last non-equal element is located on the leftmost side of the array,
    # then we can change only these elements, and the number of changes is 2
    if first_non_equal_index == len(arr) - 1 and last_non_equal_index == 0:
        return 2

    # If the first non-equal element is located on the leftmost side of the array
    # and the last non-equal element is located on the rightmost side of the array,
    # then we can change only these elements, and the number of changes is 2
    if first_non_equal_index == 0 and last_non_equal_index == len(arr) - 1:
        return 2

    # If the first non-equal element is located somewhere in the middle of the array
    # and the last non-equal element is located somewhere in the middle of the array,
    # then we can change only these elements, and the number of changes is 2
    if first_non_equal_index >= 1 and first_non_equal_index < len(arr) - 1:
        if last_non_equal_index >= 1 and last_non_equal_index < len(arr) - 1:
            return 2

    # If the first non-equal element is located on the leftmost side of the array
    # and the last non-equal element is located somewhere in the middle of the array,
    # then we can change only these elements, and the number of changes is 3
    if first_non_equal_index == 0 and last_non_equal_index >= 1 and last_non_equal_index < len(arr) - 1:
        return 3

    # If the first non-equal element is located somewhere in the middle of the array
    #

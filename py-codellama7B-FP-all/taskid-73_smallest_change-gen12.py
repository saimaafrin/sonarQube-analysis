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

    # time complexity: O(n)
    # space complexity: O(n)
    n = len(arr)
    # check for even length array
    if n % 2 == 0:
        # if the length of the array is even, then the middle index is n // 2
        # instead of n // 2 - 1 or n // 2 + 1
        # because the length of the array is even, there's no need to check for the edge cases
        middle_index = n // 2
    else:
        middle_index = n // 2 + 1

    min_changes = 0
    # two pointers, one from the beginning and one from the end
    left = 0
    right = n - 1
    while left < middle_index and right > middle_index:
        if arr[left] == arr[right]:
            # the elements are equal, move both pointers to the right
            left += 1
            right -= 1
        else:
            # the elements are not equal
            min_changes += 1
            # since the array is not palindromic, the smallest change is to change one element to make the array palindromic
            # and that element can be either the element in the left or the element in the right
            left += 1
            right -= 1

    # now, check the edge case for the left
    if left < middle_index:
        # the left pointer is not at the middle index
        # because the left pointer is at the beginning of the array,
        # then the right pointer is at the end of the array
        # and there are still elements to the left of the middle index
        # so, we need to check if the left element is equal to the right element
        if arr[middle_index] != arr[right]:
            # if the left element is not equal to the right element
            # then, we need to change the element in the left
            # because the middle element is the same, then the element on the left is different from the element on the right
            min_changes += 1

    # now, check the edge case for the right
    if right > middle_index:
        # the right pointer is not at the middle index
        # because the right pointer is at the end of the array,
        # then the left pointer is at the beginning of the array
        # and there are still elements to the right of the middle index
        # so, we need to check if the right element is equal to the left element
        if arr[middle_index] != arr[left]:
            # if the right element is not equal to the left element
            # then, we need to change the element in the right
            # because the middle element is the same, then the element on the right is different from the element on the left
            min_changes += 1

    return min_changes

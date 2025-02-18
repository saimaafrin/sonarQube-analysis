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

    # O(n) solution
    # Create a new array that has the same elements as the old array
    # but has the elements in the correct order.
    new_arr = []
    for i in range(len(arr)):
        new_arr.append(arr[i])
    # Reverse the new array
    new_arr.reverse()
    # Now that we have the array in the correct order, compare
    # element by element, and if they are not the same, change
    # the element in the array.
    count = 0
    for i in range(len(arr)):
        if arr[i] != new_arr[i]:
            count += 1
    return count

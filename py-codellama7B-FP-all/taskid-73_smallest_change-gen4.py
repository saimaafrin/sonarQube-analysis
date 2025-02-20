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


    # The algorithm works by first finding the maximum and minimum values in the array.
    # Then we create two arrays of the same length with the maximum value and the minimum value
    # repeated equal number of times. Then we create another array of the same length as the original
    # array with all values equal to 0. Finally we iterate through the original array and for each
    # element we check if its value is already in the max or min array. If it is not then we
    # increase the number of elements we need to change by one.
    #
    # Time: O(n^2)
    # Space: O(n)
    max_value = max(arr)
    min_value = min(arr)
    max_count = arr.count(max_value)
    min_count = arr.count(min_value)
    if max_count == min_count:
        return 0

    # We want the max value to be repeated max_count/2 times
    if max_count > min_count:
        max_count = (max_count + 1) // 2
    else:
        min_count = (min_count + 1) // 2

    if max_count > 0:
        arr = arr[:] + [max_value] * max_count
    if min_count > 0:
        arr = [min_value] * min_count + arr

    # Time: O(n^2)
    # Space: O(n)
    count = 0
    for i in range(len(arr)):
        if arr[i] != arr[len(arr) - 1 - i]:
            count += 1
    return count

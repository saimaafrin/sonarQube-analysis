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


    if len(arr) <= 1:
        return 0

    # 1. Calculate the difference between the element and its index.
    # 2. Get the difference list.
    # 3. Find the absolute difference between the elements.
    # 4. Find the minimum absolute difference between elements.

    # 1. Calculate the difference between the element and its index.
    diff_list = [(arr[i], i) for i in range(len(arr))]

    # 2. Get the difference list.
    diff_list = [diff[0] - diff[1] for diff in diff_list]

    # 3. Find the absolute difference between the elements.
    diff_list = [abs(diff) for diff in diff_list]

    # 4. Find the minimum absolute difference between elements.
    return min(diff_list)

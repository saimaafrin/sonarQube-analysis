from typing import List

def sort_array(array: List[int]) -> List[int]:
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.

    Note:
    * don't change the given array.

    Examples:
    >>> sort_array([])
    []
    >>> sort_array([5])
    [5]
    >>> sort_array([2, 4, 3, 0, 1, 5])
    [0, 1, 2, 3, 4, 5]
    >>> sort_array([2, 4, 3, 0, 1, 5, 6])
    [6, 5, 4, 3, 2, 1, 0]
    """

    if not array:
        return []
    sorted_array = sorted(array)
    sum_of_first_and_last = sum(array[:1] + array[-1:])
    if sum_of_first_and_last % 2:
        return sorted_array
    return sorted_array[::-1]

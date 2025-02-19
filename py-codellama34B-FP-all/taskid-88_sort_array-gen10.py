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


    def _sort_array(arr: List[int], reverse: bool = False) -> List[int]:
        return sorted(arr, reverse=reverse)

    # if array is empty
    if not array:
        return array

    # if array has only one element
    if len(array) == 1:
        return array

    # if the sum of first and last index is odd
    if array[0] + array[-1] % 2 != 0:
        return _sort_array(array)
    # if the sum of first and last index is even
    else:
        return _sort_array(array, reverse=True)

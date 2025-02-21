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


    # create a copy of the array
    copy_of_array = array.copy()

    # sort the copied array
    copy_of_array.sort()

    # if the sum of the first and last value is even sort the array in descending order
    if (copy_of_array[0] + copy_of_array[-1]) % 2 == 0:
        copy_of_array.reverse()

    return copy_of_array

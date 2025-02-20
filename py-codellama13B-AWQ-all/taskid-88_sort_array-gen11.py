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


    def sum_first_last_indexes(arr: List[int]) -> int:
        if len(arr) < 2:
            return 0
        return arr[0] + arr[-1]

    def sort_ascending(arr: List[int]) -> List[int]:
        return sorted(arr)

    def sort_descending(arr: List[int]) -> List[int]:
        return sorted(arr, reverse=True)

    sorted_array = array[:]

    if sum_first_last_indexes(sorted_array) % 2 == 0:
        sorted_array = sort_descending(sorted_array)
    else:
        sorted_array = sort_ascending(sorted_array)

    return sorted_array

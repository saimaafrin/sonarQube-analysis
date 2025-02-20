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

    def _sort(array: List[int], low: int, high: int, is_ascending: bool):
        if low >= high:
            return
        pivot = array[high]
        l = low
        for i in range(low, high):
            if array[i] <= pivot:
                array[l], array[i] = array[i], array[l]
                l += 1
        array[l], array[high] = array[high], array[l]
        _sort(array, low, l-1, is_ascending)
        _sort(array, l+1, high, is_ascending)

    total = sum(array)
    is_ascending = total % 2 == 1
    _sort(array, 0, len(array)-1, is_ascending)
    return array

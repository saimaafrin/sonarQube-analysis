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


    if len(array) < 2:
        return array.copy()

    # sort the input in ascending order
    def sort_ascending(arr: List[int]) -> List[int]:
        """
        Sort the given array in ascending order
        """
        i, j = 0, len(arr) - 1
        while i < j:
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        return arr

    # sort the input in descending order
    def sort_descending(arr: List[int]) -> List[int]:
        """
        Sort the given array in descending order
        """
        i, j = 0, len(arr) - 1
        while i < j:
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        return arr

    # sum of the first and the last elements in the array
    sum_first_last = array[0] + array[-1]

    # if the sum is odd, sort the input in ascending order
    if sum_first_last % 2:
        return sort_ascending(array.copy())

    # if the sum is even, sort the input in descending order
    return sort_descending(array.copy())

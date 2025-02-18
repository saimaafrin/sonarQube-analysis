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
        return array

    def is_sorted(array: List[int]) -> bool:
        """Check if array is sorted ascending or descending."""
        if len(array) == 1:
            return True

        if array[0] > array[-1]:
            return True

        if array[0] < array[-1]:
            return False

        return is_sorted(array[1:])

    # check if array is sorted
    if is_sorted(array):
        return array

    def swap(array: List[int], i: int, j: int) -> None:
        """Swap two elements."""
        array[i], array[j] = array[j], array[i]

    def sort_ascending(array: List[int], i: int = 0) -> List[int]:
        """Sort array in ascending order."""
        if i == len(array) - 1:
            return array

        if array[i] > array[i + 1]:
            swap(array, i, i + 1)

        return sort_ascending(array, i + 1)

    def sort_descending(array: List[int], i: int = 0) -> List[int]:
        """Sort array in descending order."""
        if i == len(array) - 1:
            return array

        if array[i] < array[i + 1]:
            swap(array, i, i + 1)

        return sort_descending(array, i + 1)

    # check the sum of first and last index of array
    if array[0] + array[-1] % 2 == 0:
        return sort_descending(array)
    else:
        return sort_ascending(array)

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

    def sort_array_asc(array: List[int]) -> List[int]:
        """
        Sort array in ascending order.
        """
        return sorted(array)

    def sort_array_desc(array: List[int]) -> List[int]:
        """
        Sort array in descending order.
        """
        return sorted(array, reverse=True)

    # don't change the given array.
    array = array.copy()
    if len(array) <= 1:
        return array

    if sum(array[0], array[-1]) % 2 == 0:
        return sort_array_desc(array)
    else:
        return sort_array_asc(array)

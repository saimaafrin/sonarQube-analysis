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


    # Check if the given array is empty
    if len(array) == 0:
        return []

    # Check if the given array has only one element
    if len(array) == 1:
        return array

    # Get the sum of the first and last elements
    first_element = array[0]
    last_element = array[-1]
    sum_first_last = first_element + last_element

    # Check if the sum is even or odd
    if sum_first_last % 2 == 0:
        # Sort the given array in descending order
        array.sort(reverse=True)
    else:
        # Sort the given array in ascending order
        array.sort()

    # Return the sorted array
    return array

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

    result = []
    for i in range(len(array)):
        if (i == 0 and sum(array[:1]) % 2 != 0) or \
                (i == len(array) - 1 and sum(array[i-1:]) % 2 != 0) or \
                (i > 0 and i < len(array) - 1 and sum(array[i-1:i+1]) % 2 != 0):
            result.append(min(array))
            array.remove(min(array))
        else:
            result.append(max(array))
            array.remove(max(array))

    return result

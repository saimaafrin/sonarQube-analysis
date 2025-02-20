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

    def sort(l, r):
        if l > r:
            return

        left_sum = sum(array[l:r])
        if left_sum % 2 == 1:
            array[l:r].sort(reverse=True)
        else:
            array[l:r].sort()

        sort(l + 1, r - 1)

    sort(0, len(array) - 1)
    return array

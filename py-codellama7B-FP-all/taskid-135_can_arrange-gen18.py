from typing import List

def can_arrange(arr: List[int]) -> int:
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    >>> can_arrange([1, 2, 4, 3, 5])
    3
    >>> can_arrange([1, 2, 3])
    -1
    """


    def largest_index_less_than_previous(arr: List[int]) -> int:
        """Create a function which returns the largest index of an element
        which is not greater than or equal to the element immediately
        preceding it. If no such element exists then return -1.

        Examples:
        >>> largest_index_less_than_previous([1, 2, 4, 3, 5])
        3
        >>> largest_index_less_than_previous([1, 2, 3])
        -1
        """
        largest = -1
        previous = -1
        for index, element in enumerate(arr):
            if element <= previous:
                largest = index
            else:
                previous = element
        return largest

    largest = largest_index_less_than_previous(arr)
    return largest if arr[largest] == arr[-1] else -1

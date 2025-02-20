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

    previous_value = 0
    current_index = len(arr) - 1

    while current_index > 0:
        current_value = arr[current_index]
        if current_value >= previous_value:
            return current_index
        previous_value = current_value
        current_index -= 1

    return -1

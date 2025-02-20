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

    result = -1
    if len(arr) == 1:
        result = 0
    elif len(arr) > 1:
        for idx, element in enumerate(arr[:-1]):
            try:
                if arr[idx] >= arr[idx + 1]:
                    break
            except IndexError:
                pass
            else:
                result = idx
    return result

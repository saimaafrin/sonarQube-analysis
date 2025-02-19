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


    # TODO: Implement this function
    # raise NotImplementedError
    arr_len = len(arr)

    if arr_len < 2:
        return -1

    max_idx = -1
    for i in range(arr_len-1, 0, -1):
        if arr[i] < arr[i-1]:
            max_idx = i-1
            break

    if max_idx == -1:
        return -1

    for i in range(max_idx-1, -1, -1):
        if arr[i] > arr[max_idx]:
            return max_idx

    return -1

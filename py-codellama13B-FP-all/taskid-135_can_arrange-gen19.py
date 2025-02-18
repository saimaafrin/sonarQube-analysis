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

    count_arr = [0] * (len(arr) + 1)
    for el in arr:
        count_arr[el] += 1

    print(count_arr)

    if count_arr[0] > 0:
        return 0

    for i in range(1, len(count_arr) - 1):
        if count_arr[i] > 0:
            if count_arr[i - 1] > 0:
                count_arr[i] -= 1
                count_arr[i - 1] -= 1
            elif count_arr[i + 1] > 0:
                count_arr[i] -= 1
                count_arr[i + 1] -= 1

    print(count_arr)

    for i in range(1, len(count_arr)):
        if count_arr[i] > 0:
            return i - 1

    return -1

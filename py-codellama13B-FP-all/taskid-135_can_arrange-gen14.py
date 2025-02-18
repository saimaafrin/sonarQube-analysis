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

    sum_arr = sum(arr)
    min_element = min(arr)
    max_element = max(arr)
    if min_element < 0 or (sum_arr - min_element) % 2 == 1:
        return -1

    half_sum = (sum_arr - min_element) // 2
    if min_element != 0:
        if min_element != half_sum:
            return -1
        else:
            return min_element
    elif min_element == 0 and half_sum == 0:
        return 0

    for i in range(len(arr)):
        diff = abs(half_sum - arr[i])
        if diff != 0 and diff % 2 == 1:
            return -1

    return arr.index(half_sum)

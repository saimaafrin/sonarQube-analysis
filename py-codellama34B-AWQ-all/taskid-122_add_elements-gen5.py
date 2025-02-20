from typing import List

def add_elements(arr: List[int], k: int) -> int:
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

    >>> add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4)
    24

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """


    if not arr:
        raise ValueError("empty array")
    if k < 1 or k > len(arr):
        raise ValueError("invalid k")

    arr = sorted(arr)
    arr_len = len(arr)
    result = 0

    for i in range(k):
        element = arr[i]
        if element < 10:
            result += element
        elif element < 100:
            result += element
            if i + 1 < k:
                result += arr[i + 1]
                i += 1
        else:
            result += arr[i - 1]
            i -= 1

    return result

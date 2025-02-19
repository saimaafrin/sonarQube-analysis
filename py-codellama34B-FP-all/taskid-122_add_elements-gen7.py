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


    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return arr[0] + arr[1]

    max_value = 0
    for i in range(k):
        max_value = max(max_value, arr[i])
        if max_value > 99:
            break

    if max_value > 99:
        return arr[0] + arr[1]
    else:
        return arr[0] + arr[1] + arr[2]

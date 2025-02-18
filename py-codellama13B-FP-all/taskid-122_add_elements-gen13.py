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

    if k == 0:
        return 0
    k = min(k, len(arr))
    res = 0
    i = 0
    while i < k:
        temp = arr[i]
        res += temp % 10
        if temp // 10 != 0:
            if i + 1 < k:
                res += temp // 10 % 10
            else:
                res += temp // 10
        i += 1
    return res

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


    if len(arr) == 0:
        return 0

    if k == 1:
        return arr[0]

    if len(arr) == k:
        return sum(arr)

    if len(str(arr[0])) <= 2:
        return arr[0] + add_elements(arr[1:], k - 1)
    else:
        return add_elements(arr[1:], k)

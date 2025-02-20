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

    result = 0

    for index, value in enumerate(arr):
        if index < k:
            if len(str(value)) <= 2:
                result += value
            elif len(str(value)) == 3:
                result += int(str(value)[:1])
            else:
                result += int(str(value)[:2])

    return result

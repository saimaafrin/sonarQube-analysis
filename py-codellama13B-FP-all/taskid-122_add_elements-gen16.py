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

    max_length = 2
    total = 0

    # First pass
    for i in range(k):
        if len(str(arr[i])) <= max_length:
            total += arr[i]

    # Second pass
    for i in range(k, len(arr)):
        if len(str(arr[i])) > max_length:
            continue

        total += arr[i]

    return total

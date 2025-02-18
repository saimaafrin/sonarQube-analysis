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

    # get the first k elements
    if k > len(arr):
        k = len(arr)

    # sum the first k elements
    total = 0
    for num in arr[:k]:
        total += num

    # sum any two-digit numbers
    for num in arr[:k]:
        if num >= 10 and num < 100:
            total += num % 10
            total += num // 10

    return total

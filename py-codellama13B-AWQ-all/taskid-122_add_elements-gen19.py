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

    max_digits = 0
    num_digits = 0

    for i in range(k):
        num_digits = 1
        num = arr[i]

        while num > 9:
            num = num // 10
            num_digits += 1

        max_digits = max(max_digits, num_digits)

    total = 0

    for i in range(min(k, len(arr))):
        total += arr[i]

    return total

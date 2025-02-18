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


    if k <= 0:
        return 0
    elif k >= len(arr):
        return sum(arr)
    else:
        digits = {}
        for i in range(k):
            digits[arr[i] % 10] = digits.get(arr[i] % 10, 0) + 1
        max_digit = max(digits.keys())
        sum_val = 0
        for i in range(1, max_digit + 1):
            sum_val += digits[i] * (10 ** (i - 1))
        return sum_val

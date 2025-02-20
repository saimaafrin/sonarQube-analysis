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

    first_k = arr[:k]
    max_digits = 2
    sum = 0

    for num in first_k:
        digits = len(str(num))
        if digits <= max_digits:
            sum += num
        else:
            break

    return sum

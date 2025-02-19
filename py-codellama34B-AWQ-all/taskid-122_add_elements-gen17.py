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

    # Find the sum of the first k elements of arr
    sum_first_k = sum(arr[:k])
    # Get the maximum number of digits
    max_digits = max(len(str(number)) for number in arr[:k])
    # Only keep the numbers with at most 2 digits
    sum_at_most_2_digits = sum(number for number in arr[:k] if len(str(number)) <= 2)
    return sum_at_most_2_digits if max_digits <= 2 else sum_first_k - sum_at_most_2_digits

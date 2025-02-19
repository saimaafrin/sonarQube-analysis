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


    k -= 1
    k = min(k, len(arr) - 1)

    k_sum = sum(arr[:k])
    two_digits = 0

    for i in range(k, len(arr)):
        element = arr[i]
        if element > 99:
            two_digits += element % 100
            element = element - two_digits
        k_sum += element

    return k_sum

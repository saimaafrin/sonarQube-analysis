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

    # Your code here
    def get_digits(n: int) -> int:
        if n < 10:
            return 1
        if n < 100:
            return 2
        return 3
    arr.sort(key = get_digits)
    result = 0
    for i, n in enumerate(arr):
        if i < k:
            result += n
        else:
            break
    return result

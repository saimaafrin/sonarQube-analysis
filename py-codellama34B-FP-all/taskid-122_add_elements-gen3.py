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

    arr = sorted(arr)[:k]
    # print(arr)
    sum = 0
    for i in arr:
        if i < 10:
            sum += i
        elif i < 100:
            sum += i // 10
            sum += i % 10
        else:
            sum += i // 100
            sum += i % 100 // 10
            sum += i % 10
    return sum

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


    # 1. Add the first k elements to sum.
    sum = 0
    for i in range(k):
        sum += arr[i]

    # 2. Check if the sum is greater than k,
    # if sum > k:
    #   Return sum.

    # 3. Otherwise, add the elements with two digits.
    # for i in range(k, len(arr)):
    #   if len(arr[i]) == 2:
    #     sum += arr[i]

    return sum

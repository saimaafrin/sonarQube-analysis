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

    # initialize the sum to 0
    sum = 0

    # loop through the first k elements of the array
    for i in range(k):
        # if the absolute value of the current element is less than or equal to 99, add it to the sum
        if abs(arr[i]) <= 99:
            sum += arr[i]

    return sum

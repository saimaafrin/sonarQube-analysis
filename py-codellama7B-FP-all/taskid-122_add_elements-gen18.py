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

    # Solution:
    # Loop from i = 0 to i < k and for each i, sum up the digits of each element
    #    arr[i] up to 2 digits.
    # If sum is greater than 9, add 1 to it.
    # Return the sum.
    #
    # Time Complexity: O(k)
    # Space Complexity: O(1)

    # Sum up the elements
    sum = 0
    for i in range(k):
        sum += (arr[i] % 10) + (arr[i] // 10)
        if sum > 9:
            sum += 1
    return sum

from typing import List

def minSubArraySum(nums: List[int]) -> int:
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    >>> minSubArraySum([2, 3, 4, 1, 2, 4])
    1
    >>> minSubArraySum([-1, -2, -3])
    -6
    """

    # O(n) time | O(1) space
    minSum = float('inf')
    currSum = 0
    for num in nums:
        currSum += num
        if currSum < minSum:
            minSum = currSum
    return minSum

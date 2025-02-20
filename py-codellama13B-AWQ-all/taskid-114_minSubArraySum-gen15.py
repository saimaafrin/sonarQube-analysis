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

    n = len(nums)
    if n == 0:
        return 0
    windowSum = 0
    windowStart = 0
    minSum = nums[0]
    for windowEnd in range(n):
        windowSum += nums[windowEnd]
        while windowSum >= minSum:
            minSum = min(minSum, windowSum)
            windowSum -= nums[windowStart]
            windowStart += 1
    return minSum

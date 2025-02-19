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
    dp = [0] * n
    min_val = float('inf')
    for i in range(n):
        dp[i] = nums[i] + (0 if i == 0 else dp[i-1])
        min_val = min(min_val, dp[i])
    return min_val

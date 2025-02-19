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

    # min sum = max (nums[i] - nums[j])
    # min sum = max (nums[i] - nums[j])
    # for every 0 <= i < j <= n

    # min_sum = max(nums[i] - nums[j])
    # for 0 <= i < j <= n

    # max(nums) - min(nums)

    return max(nums) - min(nums)

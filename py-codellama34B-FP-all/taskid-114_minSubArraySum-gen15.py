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

    total_sum = sum(nums)
    min_sum = total_sum
    for i in range(1, len(nums)):
        min_sum = min(min_sum, total_sum - sum(nums[i:]))
    return min_sum

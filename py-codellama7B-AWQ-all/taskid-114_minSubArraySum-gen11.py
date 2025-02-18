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

    min_sum = float("inf")
    sum_ = 0
    n = len(nums)
    for i in range(n):
        sum_ += nums[i]
        if i >= 1:
            sum_ -= nums[i - 1]
        min_sum = min(min_sum, sum_)
    return min_sum

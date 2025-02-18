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

    window_sum = 0
    min_sum = nums[0]
    for i in range(len(nums)):
        window_sum += nums[i]
        if i >= 1:
            min_sum = min(min_sum, window_sum - nums[i-1])
        else:
            min_sum = min(min_sum, window_sum)
    return min_sum

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

    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
    min_sum = sum
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sum = sum - nums[i] + nums[j]
            min_sum = min(sum, min_sum)
    return min_sum

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

    min_sub_sum = float('inf')
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
        min_sub_sum = min(sum, min_sub_sum)
        if sum < 0:
            sum = 0
    return min_sub_sum

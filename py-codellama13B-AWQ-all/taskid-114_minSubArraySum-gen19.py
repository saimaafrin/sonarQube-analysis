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

    min_sum = float('inf')
    for i in range(len(nums)):
        sum_curr = 0
        for j in range(i, len(nums)):
            sum_curr += nums[j]
            if sum_curr < min_sum:
                min_sum = sum_curr
    return min_sum

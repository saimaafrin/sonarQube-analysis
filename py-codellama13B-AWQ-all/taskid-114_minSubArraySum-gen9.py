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


    min_sum = sum(nums)
    current_sum = 0

    for i, _ in enumerate(nums):
        current_sum += nums[i]
        if i >= 0:
            min_sum = min(min_sum, current_sum)

    return min_sum

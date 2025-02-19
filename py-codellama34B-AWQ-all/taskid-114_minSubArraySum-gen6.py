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
    start_index = 0
    for i in range(len(nums)):
        if nums[i] < min_sum:
            min_sum = nums[i]
            start_index = i

    for i in range(len(nums)):
        if nums[i] + nums[i-1] < min_sum:
            min_sum = nums[i] + nums[i-1]

    return min_sum

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
    min_sum = float('inf')

    for i in range(len(nums)):
        window_sum += nums[i]

        if i >= 0:
            min_sum = min(min_sum, window_sum)
        if window_sum >= min_sum:
            window_sum = 0

    return min_sum

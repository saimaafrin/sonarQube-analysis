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
    window_start = 0
    for window_end in range(len(nums)):
        window_sum += nums[window_end]
        if window_end - window_start + 1 >= len(nums):
            min_sum = min(min_sum, window_sum)
            window_sum -= nums[window_start]
            window_start += 1
    return min_sum

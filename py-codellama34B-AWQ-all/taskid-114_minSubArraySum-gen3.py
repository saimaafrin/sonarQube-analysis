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


    window = 0
    min_window = 999999999

    for i in range(len(nums)):
        window += nums[i]
        if window < min_window:
            min_window = window
        if i < len(nums) - 1:
            window -= nums[i+1]

    return min_window

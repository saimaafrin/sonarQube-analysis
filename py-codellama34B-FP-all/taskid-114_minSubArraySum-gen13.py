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

    # find the minimum sum of any non-empty sub-array
    # sliding window
    window_min = 100000
    window_sum = 0

    for num in nums:
        window_sum += num
        if window_sum < window_min:
            window_min = window_sum
        elif window_sum - num < window_min:
            window_min = window_sum - num

    return window_min

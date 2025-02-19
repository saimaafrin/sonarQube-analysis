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

    # initialize window end and min window sum
    min_sum = float('inf')
    window_end = 0

    for window_start in range(len(nums)):
        # shrink window if the current element is lesser than the smallest element
        while window_end < len(nums) and nums[window_end] < nums[window_start]:
            window_end += 1

        # save the minimum sum
        min_sum = min(min_sum, sum(nums[window_start: window_end]))

    return min_sum

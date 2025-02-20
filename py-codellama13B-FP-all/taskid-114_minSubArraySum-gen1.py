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

    if not nums:
        return 0
    window_start = 0
    window_sum = 0
    min_sum = float('inf')
    for window_end in range(len(nums)):
        window_sum += nums[window_end]
        if window_end >= 0 and window_sum >= min_sum:
            min_sum = min(min_sum, window_sum)
        if window_end >= 0 and window_end - window_start + 1 >= 1:
            window_sum -= nums[window_start]
            window_start += 1
    return min_sum if min_sum != float('inf') else 0

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

    n = len(nums)
    if n == 1:
        return nums[0]
    min_sum = float('inf')
    for i in range(n):
        if i < n - 1:
            min_sum = min(min_sum, nums[i] + nums[i+1])
        if i < n - 2:
            min_sum = min(min_sum, nums[i] + nums[i+1] + nums[i+2])
    return min_sum

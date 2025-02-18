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

    i, j = 0, 0
    min_sum = 0
    while j < len(nums):
        min_sum = min(min_sum, sum(nums[i:j + 1]))
        j += 1
        if min_sum == sum(nums[i:j + 1]):
            i += 1
    return min_sum

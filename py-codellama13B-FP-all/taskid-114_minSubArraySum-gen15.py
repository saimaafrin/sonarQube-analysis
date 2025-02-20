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
    if n == 2:
        return min(nums[0], nums[1])
    return min(nums[0], min(nums[1], minSubArraySum(nums[2:])))

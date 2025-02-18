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

    s = sum(nums)
    min_s = s
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            s = sum(nums[i:j])
            if s < min_s:
                min_s = s
    return min_s

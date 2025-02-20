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

    # Find the min sum of a sub array
    for i in range(len(nums)):
        if sum(nums[i:]) < sum(nums[:i]):
            return sum(nums[i:])
    return sum(nums)

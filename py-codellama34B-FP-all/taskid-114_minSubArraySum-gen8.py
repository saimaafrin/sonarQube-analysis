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
        raise ValueError("nums must be a list of int")
    res = 2**31-1
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            res = min(res, sum(nums[i:j+1]))
    return res

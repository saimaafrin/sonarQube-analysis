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

    total = 0
    res = 10000

    for num in nums:
        total += num
        if total >= res:
            res = total
        elif total < 0:
            total = 0

    return res

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
    if n == 0:
        return 0

    ans = nums[0]
    s = 0
    for i in range(1, n):
        s += nums[i]
        ans = min(ans, s)
    return ans

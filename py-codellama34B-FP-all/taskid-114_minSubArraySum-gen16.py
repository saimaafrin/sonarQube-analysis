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
    ans = float('inf')

    for i in range(n):
        cur = 0
        for j in range(i, n):
            cur += nums[j]
            ans = min(ans, cur)
    return ans

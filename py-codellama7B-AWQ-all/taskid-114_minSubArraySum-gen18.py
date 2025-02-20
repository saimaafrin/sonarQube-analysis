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

    if not nums: return 0
    minSum = sum(nums)
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sum = sum(nums[i:j+1])
            if sum < minSum:
                minSum = sum
    return minSum

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
    result = float('inf')

    for i in range(len(nums)):
        total += nums[i]
        for j in range(i + 1, len(nums)):
            total += nums[j]
            result = min(result, total)
            total -= nums[i]

    return result

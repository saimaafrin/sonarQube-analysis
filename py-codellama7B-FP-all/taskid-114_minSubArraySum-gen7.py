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
    total = 0
    min_sum = float("inf")

    while j < len(nums):
        total += nums[j]
        min_sum = min(min_sum, total)

        while total >= nums[i]:
            total -= nums[i]
            i += 1

        j += 1

    return min_sum

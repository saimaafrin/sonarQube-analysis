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

    left, right = 0, 0
    total = 0
    min_sum = float('inf')
    while right < len(nums):
        total += nums[right]
        right += 1
        while left < right and total >= 0:
            total -= nums[left]
            left += 1
        min_sum = min(min_sum, total)
    return min_sum

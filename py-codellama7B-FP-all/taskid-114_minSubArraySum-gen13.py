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

    left = 0
    right = 0
    min_sum = float('inf')
    current_sum = 0

    while right < len(nums):
        current_sum += nums[right]
        while current_sum > 0:
            min_sum = min(min_sum, current_sum)
            current_sum -= nums[left]
            left += 1
        right += 1

    return min_sum

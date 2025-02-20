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

    if len(nums) == 0:
        return 0
    minSum = sum(nums)
    left = 0
    right = 0
    currentSum = 0
    while left < len(nums) and right < len(nums):
        currentSum += nums[right]
        while currentSum < minSum and left < len(nums):
            minSum = currentSum
            left += 1
            currentSum = sum(nums[left:right+1])
        right += 1
    return minSum

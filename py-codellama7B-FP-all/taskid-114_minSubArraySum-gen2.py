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

    # Find the sum of the minimum sub-array
    # -------------------------------------
    # We need to start from the minimum element
    # and add the following numbers until the
    # sum is not negative
    min_sum = sum(nums)
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if sum(nums[i:j+1]) < min_sum:
                min_sum = sum(nums[i:j+1])
    return min_sum

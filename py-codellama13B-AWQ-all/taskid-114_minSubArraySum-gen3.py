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

    # Solution 1:
    # 1. Brute Force
    # 2. Sliding Window
    # 3. Divide and Conquer
    # 4. Greedy
    # Solution 2:
    # 1. Prefix Sum
    total = sum(nums)
    if total < 0: return total

    min_sum = total
    for i in range(len(nums)):
        total -= nums[i]
        if total < min_sum:
            min_sum = total
    return min_sum

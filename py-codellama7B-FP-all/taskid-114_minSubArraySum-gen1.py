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


    if not nums:
        return 0

    min_sum = sum(nums)
    j = 0
    for i in range(1, len(nums)):
        while sum(nums[j:i]) > min_sum:
            min_sum = min(sum(nums[j:i]), min_sum)
            j += 1

    return min_sum

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


    running_sum = 0
    min_sum = 10 ** 8
    for num in nums:
        running_sum += num
        if running_sum < min_sum:
            min_sum = running_sum
        elif running_sum - min_sum > 0:
            running_sum = min_sum

    return min_sum

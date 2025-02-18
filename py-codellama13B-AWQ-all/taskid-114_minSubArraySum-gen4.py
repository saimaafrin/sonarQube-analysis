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

    # minSum = float('inf')
    # for i in range(len(nums)):
    #     for j in range(i, len(nums)):
    #         minSum = min(minSum, sum(nums[i:j+1]))
    # return minSum

    # brute force
    # min_sum = float('inf')
    # for i in range(len(nums)):
    #     for j in range(i, len(nums)):
    #         sum_ = sum(nums[i:j+1])
    #         if sum_ < min_sum:
    #             min_sum = sum_
    # return min_sum

    # window
    min_sum = 0
    for i in range(len(nums)):
        min_sum += nums[i]
        if i > 0:
            min_sum -= nums[i-1]
    return min_sum

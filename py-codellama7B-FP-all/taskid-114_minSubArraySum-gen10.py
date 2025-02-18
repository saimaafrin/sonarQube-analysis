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


    # The algorithm has O(N) time complexity and O(1) space complexity.
    min_sum = float('inf')
    sum = 0

    for i in range(len(nums)):
        sum += nums[i]
        if i > 0:
            sum -= nums[i - 1]

        if sum < min_sum:
            min_sum = sum

    return min_sum if min_sum < float('inf') else 0

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

    prefix_sums = [0]
    curr_sum = 0
    for num in nums:
        curr_sum += num
        prefix_sums.append(curr_sum)

    min_sum = float('inf')
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            min_sum = min(min_sum, prefix_sums[j] - prefix_sums[i])

    return min_sum

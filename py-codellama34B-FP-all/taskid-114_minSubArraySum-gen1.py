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

    minSum = float('inf')
    prefixSums = []
    for idx, num in enumerate(nums):
        if idx == 0:
            prefixSums.append(num)
            continue

        prefixSums.append(prefixSums[idx - 1] + num)

    for idx, num in enumerate(nums):
        if idx == 0:
            minSum = min(minSum, num)
            continue

        minSum = min(minSum, prefixSums[idx] - prefixSums[idx - 1])

    return minSum

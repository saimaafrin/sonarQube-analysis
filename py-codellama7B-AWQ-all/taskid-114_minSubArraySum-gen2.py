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

    n = len(nums)
    m = n + 1
    result = float('inf')
    for i in range(n):
        j = i + 1
        while j < n:
            # print(f'sum: {sum(nums[i:j])}')
            result = min(result, sum(nums[i:j]))
            j += 1
    return result

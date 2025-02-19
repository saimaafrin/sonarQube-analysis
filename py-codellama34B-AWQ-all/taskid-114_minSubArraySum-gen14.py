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

    # Brute Force
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    minimum_sum = float('inf')
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            minimum_sum = min(minimum_sum, current_sum)

    return minimum_sum

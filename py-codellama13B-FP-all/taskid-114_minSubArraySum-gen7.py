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


    # this is a sliding window problem
    # we just need to maintain a sum and update it
    # when moving to the next index
    # O(n) time, O(1) space
    # the idea is that we keep a min of all of the sum
    # and we update the min as we go through the array
    # and we return min at the end
    min_sum = nums[0]
    cur_sum = 0
    for num in nums:
        cur_sum += num
        min_sum = min(min_sum, cur_sum)
    return min_sum

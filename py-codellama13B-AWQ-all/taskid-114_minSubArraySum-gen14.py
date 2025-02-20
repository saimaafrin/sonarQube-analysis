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

    # time complexity: O(n)
    # space complexity: O(1)

    # use two pointers, one pointer at the beginning of the subarray and the other at the end of the subarray
    # if the sum of the subarray is less than 1, then we return the sum
    # else we update the sum with the new value and move the pointers to the right
    # at the end we return the minimum subarray sum

    # initialize variables
    min_subarray_sum = float('inf')
    sum_subarray = 0

    # initialize pointers
    left_pointer = 0
    right_pointer = 0

    # loop through the array
    while right_pointer < len(nums):
        # add the value at the right pointer to the sum
        sum_subarray += nums[right_pointer]

        # if the sum of the subarray is less than the min_subarray_sum
        if sum_subarray < min_subarray_sum:
            # update the min_subarray_sum
            min_subarray_sum = sum_subarray

        # move the right pointer to the right
        right_pointer += 1

        # if the sum of the subarray is greater than the min_subarray_sum
        if sum_subarray > min_subarray_sum:
            # subtract the value at the left pointer from the sum
            sum_subarray -= nums[left_pointer]

            # move the left pointer to the right
            left_pointer += 1

    return min_subarray_sum

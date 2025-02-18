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

    # Initialize the minimum sum to the maximum value of an integer.
    min_sum = 2 ** 31 - 1

    # Initialize the sum to 0.
    sum_of_array = 0

    # Iterate through the array.
    for i in range(len(nums)):

        # Add the current element to the sum.
        sum_of_array += nums[i]

        # If the sum is less than the minimum sum, update the minimum sum.
        if sum_of_array < min_sum:
            min_sum = sum_of_array

        # If the sum is greater than 0, set the sum to 0 so that it doesn't effect the next sub-array.
        if sum_of_array > 0:
            sum_of_array = 0

    return min_sum

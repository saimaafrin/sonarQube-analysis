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

    # Get the minimum element of the array,
    # and the sum of all the elements of the array.
    min_val = min(nums)
    total_sum = sum(nums)

    # Set the minimum sub-array sum to be the total sum of the array.
    # The minimum sub-array sum will be updated to be the minimum value
    # if it is less than the minimum sub-array sum.
    min_sub_array_sum = total_sum

    # The sum of the sub-array is the sum of the array minus the current index
    # element.
    sub_array_sum = total_sum

    # Iterate through the array.
    for i in range(len(nums)):
        sub_array_sum = sub_array_sum - nums[i]

        # If the sub-array sum is less than the minimum sub-array sum,
        # update the minimum sub-array sum.
        if sub_array_sum < min_sub_array_sum:
            min_sub_array_sum = sub_array_sum

    # If the minimum sub-array sum is equal to the total sum of the array,
    # then set the minimum sub-array sum to be the minimum value.
    if min_sub_array_sum == total_sum:
        min_sub_array_sum = min_val

    return min_sub_array_sum

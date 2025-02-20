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


    # find the sum of all the elements in the array
    sum_array = sum(nums)

    # find the minimum element in the array
    min_element = min(nums)

    # set min_sum to the minimum possible value that can be achieved
    min_sum = min_element

    # iterate through the array
    for i in range(len(nums)):
        # set current_sum to the sum of all the elements in the array
        # starting from the current index
        current_sum = sum_array - nums[i]

        # set temp to the minimum possible value that can be achieved
        # starting from the current index
        temp = nums[i]

        # iterate through the array starting from the current index
        for j in range(i + 1, len(nums)):
            # subtract the current element from the current sum
            current_sum -= nums[j]

            # if the current element is less than the minimum value
            # then set the minimum value to the current element
            if nums[j] < temp:
                temp = nums[j]

            # if the current sum is less than the minimum possible value
            # starting from the current index, then set the minimum possible
            # value to the current sum
            if current_sum < temp:
                temp = current_sum

        # if the minimum possible value that can be achieved starting from
        # the current index is less than the minimum possible value,
        # then set the minimum possible value to the current value
        if temp < min_sum:
            min_sum = temp

    return min_sum

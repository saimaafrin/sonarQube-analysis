from typing import List

def order_by_points(nums: List[int]) -> List[int]:
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12])
    [-1, -11, 1, -12, 11]
    >>> order_by_points([])
    []
    """


    # find the sum of the digits for each item
    sums = []
    for num in nums:
        total = 0
        while num != 0:
            total += num % 10
            num = num // 10
        sums.append(total)

    # sort the list based on the sum
    sorted_list = sorted(nums, key=lambda x: sums[nums.index(x)])

    # sort based on index if sum of digits are similar
    # because python 3.7 uses Timsort by default, we don't need to implement stable sort algorithm here
    if len(nums) > 1:
        for i in range(len(nums) - 1):
            if sums[i] == sums[i + 1]:
                sorted_list[i + 1] = nums[sums[i + 1]]

    return sorted_list

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

    #sort the list with default key function
    nums.sort()
    #sort the list according to the sum of its digits
    nums.sort(key=lambda num: (num, sum(map(int, str(abs(num))))))
    #sort the list according to its index in original list
    nums.sort(key=lambda num: nums.index(num))

    return nums

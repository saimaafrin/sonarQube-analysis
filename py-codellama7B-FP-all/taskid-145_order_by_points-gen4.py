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

    def get_key(num):
        """
        Find the sum of digits in given integer.
        """
        # convert to string
        s = str(abs(num))
        # sum of digits
        sum_of_digits = sum(int(i) for i in s)
        # index in original list
        index_in_original_list = nums.index(num)
        return (sum_of_digits, index_in_original_list)

    return sorted(nums, key=get_key)

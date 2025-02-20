from typing import List

def sort_array(arr: List[int]) -> List[int]:
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4])
    [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6])
    [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4])
    [0, 1, 2, 3, 4]
    """

    if len(arr) <= 1:
        return arr
    low = [i for i in arr if i & 1 == 0]
    high = [i for i in arr if i & 1 == 1]
    low.sort()
    high.sort()
    return low + high

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


    # Step 1: Convert each number to a binary number.
    #         For example: 10 -> 0b1010, 2 -> 0b10
    binary_list = [f'{i:b}' for i in arr]

    # Step 2: Count the number of ones in each binary number.
    #         For example: 0b1010 -> 2
    #                     0b10 -> 1
    count_ones_list = [binary.count('1') for binary in binary_list]

    # Step 3: Sort the list of numbers based on the number of ones and then decimal value.
    sorted_list = sorted(arr, key=lambda x: (count_ones_list[arr.index(x)], x))

    return sorted_list

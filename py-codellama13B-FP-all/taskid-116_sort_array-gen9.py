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

    # Convert each integer to its binary representation
    binary_arr = [bin(i).count("1") for i in arr]
    # sort the array according to number of ones in binary representation
    binary_arr.sort()
    # create a new array
    sorted_arr = []
    # Add the sorted elements to the new array
    for i in range(len(binary_arr)):
        sorted_arr.append(arr[binary_arr.index(i)])
    # return the sorted array
    return sorted_arr

from typing import List

def specialFilter(nums: List[int]) -> int:
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    >>> specialFilter([15, -73, 14, -15])
    1
    >>> specialFilter([33, -2, -3, 45, 21, 109])
    2
    """

    # 1) initialize an array to keep track of elements greater than 10
    # 2) loop through the input array and check if each element is greater than 10
    # 3) check if the first and last digits of each element are odd using the modulo operator
    # 4) if both digits are odd, add that element to the array
    # 5) return the length of the array
    special_nums = []
    for i in range(len(nums)):
        if nums[i] > 10 and ((nums[i] % 10) % 2 == 1 and (nums[i] // 10) % 2 == 1):
            special_nums.append(nums[i])
    return len(special_nums)

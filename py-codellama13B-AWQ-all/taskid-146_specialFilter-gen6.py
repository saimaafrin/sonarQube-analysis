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

    odd_count = 0
    for num in nums:
        # get first and last digits
        first_digit, last_digit = str(num)[0], str(num)[-1]
        if num > 10 and first_digit.isdigit() and last_digit.isdigit():
            if first_digit == '1' or first_digit == '3' or first_digit == '5' or first_digit == '7' or first_digit == '9':
                if last_digit == '1' or last_digit == '3' or last_digit == '5' or last_digit == '7' or last_digit == '9':
                    odd_count += 1
    return odd_count

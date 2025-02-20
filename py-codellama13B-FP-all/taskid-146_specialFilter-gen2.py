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

    odd_last_digits = [1, 3, 5, 7, 9]
    odd_first_digits = [1, 3, 5, 7, 9]
    count = 0
    
    for i in nums:
        if abs(i) >= 10 and odd_last_digits.count(i % 10) > 0 and odd_first_digits.count(i // 10) > 0:
            count += 1
    
    return count

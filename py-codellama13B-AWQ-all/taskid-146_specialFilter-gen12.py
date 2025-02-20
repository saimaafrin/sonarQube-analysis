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

    
    # this is a lambda function to determine whether an integer is
    # odd.
    isOdd = lambda x: x % 2 == 1
    
    # this is a lambda function to determine whether a number is
    # greater than 10 and both first and last digits are odd
    isSpecial = lambda x: (x > 10) and (isOdd(x % 10) and isOdd(x // 10))
    
    # count the number of elements in the array that meet the criteria
    count = 0
    for x in nums:
        if isSpecial(x):
            count += 1
    
    # return the count
    return count

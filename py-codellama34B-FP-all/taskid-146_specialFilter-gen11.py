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

    return len(list(filter(lambda x: (x > 10 and x % 10 in [1,3,5,7,9] and x // 100 in [1,3,5,7,9]) if x >= 100 else (x % 10 in [1,3,5,7,9] and x // 10 in [1,3,5,7,9]), nums)))

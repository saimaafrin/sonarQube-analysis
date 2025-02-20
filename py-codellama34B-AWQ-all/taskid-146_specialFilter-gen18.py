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


    count = 0
    for num in nums:
        first = str(num)[0]
        last = str(num)[-1]
        if num > 10 and (first in '13579') and (last in '13579'):
            count += 1

    return count

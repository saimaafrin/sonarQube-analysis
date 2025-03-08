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

    counter = 0
    for num in nums:
        if len(str(num)) == 2 and str(num)[0] in ('1','3','5','7','9') \
            and str(num)[1] in ('1','3','5','7','9') and num > 10:
            counter += 1
    return counter

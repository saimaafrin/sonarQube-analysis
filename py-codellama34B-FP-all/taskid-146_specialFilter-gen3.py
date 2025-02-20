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


    def odd_digits_at_ends(num):
        """Return True if num has odd digits at both ends, False otherwise."""
        num_str = str(num)
        return num_str[0] in '13579' and num_str[-1] in '13579'

    return len([num for num in nums if odd_digits_at_ends(num) and num > 10])

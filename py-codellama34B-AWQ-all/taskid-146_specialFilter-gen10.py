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


    def oddFirstAndLastDigit(number: int) -> bool:
        """Check if the first and last digits of a number are odd.

        >>> oddFirstAndLastDigit(15)
        True
        >>> oddFirstAndLastDigit(-73)
        False
        >>> oddFirstAndLastDigit(14)
        False
        >>> oddFirstAndLastDigit(-15)
        False
        >>> oddFirstAndLastDigit(109)
        True
        >>> oddFirstAndLastDigit(45)
        False
        >>> oddFirstAndLastDigit(21)
        True
        """
        return bool(number > 10 and
                    (number // 10) % 2 == 1 and
                    number % 10 == 1)

    return sum(oddFirstAndLastDigit(number) for number in nums)

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


    # initialize a variable to store the count
    count = 0

    # loop through the array
    for i in range(len(nums)):
        # initialize a variable to store the number
        num = nums[i]

        # if the number is greater than 10
        if num > 10:
            # initialize a variable to store the first digit of the number
            first = num // 10

            # initialize a variable to store the last digit of the number
            last = num % 10

            # if the first digit is odd
            if first % 2 == 1:
                # if the last digit is odd
                if last % 2 == 1:
                    # increment the count
                    count += 1

    # return the count
    return count

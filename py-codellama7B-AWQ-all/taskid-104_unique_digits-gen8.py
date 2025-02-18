from typing import List

def unique_digits(x: List[int]) -> List[int]:
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """


    # Approach 1:
    # Solution using set.
    # set won't allow duplicates, 
    # so if any number has even digit then that number won't be added
    # to set and won't be included in output list
    # In this way we can be sure that output list has all unique numbers
    # and all numbers don't have even digits

    # Solution:
    # use set() to store numbers that don't have even digits
    # iterate over input list and check if each number has any even digit
    # if number doesn't have any even digit then add it to set
    # finally return the list of numbers from set

    # Time complexity: O(n) where n is the length of list
    # Space complexity: O(n) where n is the length of list

    # Approach 2:
    # Solution using dictionary
    # we can keep a track of numbers that have even digits
    # and then find numbers that don't have any even digit

    # Solution:
    # create a dictionary to store numbers and their digits
    # iterate over input list and check if each number has any even digit
    # if number doesn't have any even digit then add it to dictionary
    # finally return the list of numbers from dictionary

    # Time complexity: O(n) where n is the length of list
    # Space complexity: O(n) where n is the length of list

    # Approach 3:
    # Solution using Bitwise operation
    # We can find a number that has even digit by and-ing it with 11111111
    # We can find a number that doesn't have any even digit by and-ing it with 10101010
    # If result of above operations is zero then number has even digit otherwise it doesn't have any even digit

    # Solution:
    # iterate over input list and check if each number has any even digit
    # if number doesn't have any even digit then add it to output list

    # Time complexity: O(n) where n is the length of list
    # Space complexity: O(n) where n is the length of list

    # Approach 4:
    # Solution using XOR operation
    # we can find a number that has even digit by XOR-ing it with 11111111
    # we can find a number that doesn't have any even digit by XOR-ing it with 10101010
    # If result of above operations is zero then number has even digit otherwise it doesn't have any even digit

    # Solution:
    # iterate over input list and check if each number has any even digit
    # if number doesn't have any even digit then add it to output list

    # Time complexity: O(n) where n is the length of list
    # Space complexity: O(n) where n is the length of list

    # Approach 5:
    # Solution using Bitwise operation and XOR operation
    # we can find a number that has even digit by XOR-ing it with 11111111
    # we can find a number that doesn't have any even digit by and-ing it with 10101010
    # If result of above operations is zero then number has even digit otherwise it doesn't have any even digit

    # Solution:
    # iterate over input list and check if each number has any even digit
    # if number doesn't have any even digit then add it to output list

    # Time complexity: O(n) where n is the length of list
    # Space complexity: O(n) where n is the length of list
    # Approach 6:
    # Solution using dictionary
    # we can

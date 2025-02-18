from typing import List

def exchange(lst1: List[int], lst2: List[int]) -> str:
    """In this problem, you will implement a function that takes two lists of numbers,
    and determines whether it is possible to perform an exchange of elements
    between them to make lst1 a list of only even numbers.
    There is no limit on the number of exchanged elements between lst1 and lst2.
    If it is possible to exchange elements between the lst1 and lst2 to make
    all the elements of lst1 to be even, return "YES".
    Otherwise, return "NO".
    For example:
    >>> exchange([1, 2, 3, 4], [1, 2, 3, 4])
    'YES'
    >>> exchange([1, 2, 3, 4], [1, 5, 3, 4])
    'NO'
    It is assumed that the input lists will be non-empty.
    """

    # Initialize a boolean flag to indicate that we have found an odd number.
    odd_found = False

    # Iterate through each number in lst1.
    for num in lst1:
        # If the current number is odd, set the odd_found flag to True.
        if num % 2 == 1:
            odd_found = True

    # If we haven't found an odd number in lst1, return "YES"
    # because we can exchange elements between lst1 and lst2
    # to make lst1 a list of only even numbers.
    if not odd_found:
        return "YES"

    # Iterate through each number in lst1.
    for num in lst1:
        # If the current number is even, check if it is in lst2.
        # If it is, then remove it from lst2.
        if num % 2 == 0 and num in lst2:
            lst2.remove(num)

    # If all the remaining elements in lst2 are even,
    # return "YES" because we can exchange elements between lst1 and lst2
    # to make lst1 a list of only even numbers.
    # Otherwise, return "NO".
    for num in lst2:
        if num % 2 == 1:
            return "NO"
    return "YES"

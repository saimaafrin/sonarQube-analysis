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

    # Check if all the elements of lst1 are even
    if not all(x % 2 == 0 for x in lst1):
        return 'NO'
    # Check if there is an element in lst2 that is not in lst1
    if any(x not in lst1 for x in lst2):
        return 'NO'
    # Check if there is an element in lst1 that is not in lst2
    if any(x not in lst2 for x in lst1):
        return 'NO'
    # Check if there is an element in lst1 that is not even
    if any(x % 2 == 1 for x in lst2):
        return 'NO'
    # Check if there is an element in lst2 that is not even
    if any(x % 2 == 1 for x in lst1):
        return 'NO'
    # If the above conditions are met, then the exchange can be performed
    return 'YES'

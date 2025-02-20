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

    even_lst1 = [num for num in lst1 if num % 2 == 0]
    odd_lst1 = [num for num in lst1 if num % 2 != 0]

    # 1. If all the elements of lst1 are even, return YES.
    if len(odd_lst1) == 0:
        return 'YES'
    # 2. If lst2 does not contain enough even numbers to match all the odd numbers
    #    in lst1, return NO.
    elif len(even_lst1) < len(odd_lst1):
        return 'NO'
    # 3. If there are enough even numbers in lst2 to match all the odd numbers
    #    in lst1, return YES.
    else:
        return 'YES'

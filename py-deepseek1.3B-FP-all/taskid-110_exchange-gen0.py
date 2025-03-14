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

    evens_lst1 = [i for i in lst1 if i % 2 == 0]
    odds_lst1 = [i for i in lst1 if i % 2 != 0]
    evens_lst2 = [i for i in lst2 if i % 2 == 0]
    odds_lst2 = [i for i in lst2 if i % 2 != 0]

    # If both lists have an equal number of even and odd elements
    if len(evens_lst1) == len(odds_lst1) and len(evens_lst2) == len(odds_lst2):
        return 'YES'
    else:
        return 'NO'

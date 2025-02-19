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

    lst1.sort()
    lst2.sort()
    i, j = 0, 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] % 2 == 0 and lst2[j] % 2 != 0:
            lst1[i], lst2[j] = lst2[j], lst1[i]
            i += 1
        if lst1[i] % 2 != 0 and lst2[j] % 2 == 0:
            lst1[i], lst2[j] = lst2[j], lst1[i]
            j += 1
        if lst1[i] % 2 == 0 and lst2[j] % 2 == 0:
            i += 1
            j += 1
        if lst1[i] % 2 != 0 and lst2[j] % 2 != 0:
            i += 1
            j += 1
    if i == len(lst1):
        return 'NO'
    else:
        return 'YES'

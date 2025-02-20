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

    # your code here
    if len(lst1) == 0 or len(lst2) == 0:
        return "NO"
    if all(i % 2 == 0 for i in lst1) and all(i % 2 == 0 for i in lst2):
        return "YES"
    # both lists are odd
    if all(i % 2 == 1 for i in lst1) and all(i % 2 == 1 for i in lst2):
        return "NO"
    # exactly one is odd
    if len(lst1) == 1 and all(i % 2 == 0 for i in lst2):
        return "YES"
    if all(i % 2 == 0 for i in lst1) and len(lst2) == 1:
        return "YES"
    # both lists have multiple elements
    if len(lst1) == 1:
        if all(i % 2 == 0 for i in lst2):
            return "YES"
        else:
            return "NO"
    if len(lst2) == 1:
        if all(i % 2 == 0 for i in lst1):
            return "YES"
        else:
            return "NO"
    # lst1[0] % 2 != lst2[0] % 2
    if lst1[0] % 2 == lst2[0] % 2:
        return "NO"
    # lst1[0] % 2 != lst2[1] % 2
    if lst1[0] % 2 == lst2[1] % 2:
        return "NO"
    # lst1[1] % 2 != lst2[0] % 2
    if lst1[1] % 2 == lst2[0] % 2:
        return "NO"
    # lst1[1] % 2 != lst2[1] % 2
    if lst1[1] % 2 == lst2[1] % 2:
        return "NO"
    # else
    return "YES"

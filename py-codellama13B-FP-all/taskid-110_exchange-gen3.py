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

    even = []
    odd = []
    if len(lst1) != len(lst2):
        return "NO"
    for idx in range(len(lst1)):
        if lst1[idx] % 2 == 0:
            even.append(lst1[idx])
        else:
            odd.append(lst1[idx])
    for idx in range(len(lst1)):
        if lst2[idx] % 2 == 0:
            even.append(lst2[idx])
        else:
            odd.append(lst2[idx])
    if len(even) != len(lst1):
        return "NO"
    else:
        return "YES"

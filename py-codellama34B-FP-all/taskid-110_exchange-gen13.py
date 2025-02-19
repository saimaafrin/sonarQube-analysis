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

    # Your code here
    if not lst1 or not lst2:
        return "NO"
    lst1.sort()
    lst2.sort()
    if len(lst1) == 1:
        return "YES" if lst1[0] % 2 == 0 else "NO"
    if lst1[0] % 2 == 0:
        return "YES"
    if lst2[-1] % 2 == 0:
        return "YES"
    return exchange(lst1[1:], lst2[:-1])

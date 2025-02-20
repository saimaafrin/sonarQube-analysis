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

    lst1_copy = lst1.copy()
    for i in range(len(lst1_copy)):
        if lst1_copy[i] % 2 == 1:
            if lst1_copy[i] in lst2:
                lst2.remove(lst1_copy[i])
                lst1_copy[i] = lst1_copy[i] - 1
                continue
            return "NO"

    return "YES"

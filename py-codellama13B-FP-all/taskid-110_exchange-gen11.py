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

    if not (lst1 and lst2):
        raise ValueError('lists must be non-empty')

    if not all(n % 2 == 0 for n in lst1):
        return 'NO'

    def helper(lst1: List[int], lst2: List[int]) -> bool:
        if not (lst1 and lst2):
            return False

        # Exchange one element at a time, and check if lst1 is a list of even numbers
        if not lst1[0] % 2 == 0:
            if len(lst2) == 1:
                return False
            lst2 = lst2[1:]
            lst2.append(lst1[0])
            return helper(lst1[1:], lst2)

        # Recursively check if it is possible to exchange more elements
        return helper(lst1[1:], lst2)

    return 'YES' if helper(lst1, lst2) else 'NO'

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

    lst1_only_even = all(i % 2 == 0 for i in lst1)
    lst2_only_even = all(i % 2 == 0 for i in lst2)
    if lst1_only_even and lst2_only_even:
        return "YES"
    elif lst1_only_even and not lst2_only_even:
        for i in range(len(lst2)):
            if lst2[i] % 2 == 0:
                lst1[i], lst2[i] = lst2[i], lst1[i]
                break
        lst1_only_even = all(i % 2 == 0 for i in lst1)
        if lst1_only_even:
            return "YES"
    return "NO"

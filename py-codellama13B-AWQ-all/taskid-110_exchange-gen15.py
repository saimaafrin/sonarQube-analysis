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
    # lst1, lst2 = list(lst1), list(lst2)

    # if len(lst1) == 0 and len(lst2) == 0:
    #     return 'YES'

    # if len(lst1) == 0 or len(lst2) == 0:
    #     return 'NO'

    # if sum(lst1) % 2 == 0 and sum(lst2) % 2 == 0:
    #     return 'YES'

    # if sum(lst1) % 2 == 0:
    #     return 'YES'

    # if sum(lst2) % 2 == 0:
    #     return 'YES'

    # if sum(lst1) % 2 != 0 and sum(lst2) % 2 != 0:
    #     return 'NO'

    # if len(lst1) > len(lst2):
    #     lst2.extend(lst1[:len(lst1) - len(lst2)])
    #     lst1 = lst1[:len(lst2)]

    # elif len(lst2) > len(lst1):
    #     lst1.extend(lst2[:len(lst2) - len(lst1)])
    #     lst2 = lst2[:len(lst1)]

    # while len(lst1) > 0:
    #     if sum(lst1) % 2 == 0 and sum(lst2) % 2 == 0:
    #         return 'YES'

    #     lst1.pop(0)
    #     lst2.pop(0)

    # return 'NO'

    # return "YES" if sum(lst1) % 2 == 0 and sum(lst2) % 2 == 0 else "NO"

    lst1, lst2 = list(lst1), list(lst2)

    if not lst1 and not lst2:
        return 'YES'

    if not lst1 or not lst2:
        return 'NO'

    if sum(lst1) % 2 == 0 and sum(lst2) % 2 == 0:
        return 'YES'

    if sum(lst1) % 2 == 0:
        return 'YES'

    if sum(lst2) % 2 == 0:
        return 'YES'

    return 'NO'

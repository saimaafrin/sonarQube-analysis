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

    if not (len(lst1) and len(lst2)):
        raise ValueError("The length of the list should be non-zero")

    if not all(isinstance(x, int) for x in lst1) or not all(isinstance(x, int) for x in lst2):
        raise ValueError("The elements of the list should be an integer")

    if len(lst1) != len(lst2):
        raise ValueError("The length of the list is different")

    # The first element of lst1 and lst2 should be equal
    if lst1[0] != lst2[0]:
        return "NO"

    for idx, val in enumerate(lst1):
        if val % 2 == 1:
            # If the value of the element in lst1 is odd,
            # the exchange operation between lst1 and lst2 is impossible
            if val % 2 == 1:
                return "NO"

            # If the value of the element in lst1 is even,
            # the exchange operation is possible.
            # In this case, the value of the element in lst2 should be equal to the value of the element in lst1.
            if val != lst2[idx]:
                return "NO"

    return "YES"
